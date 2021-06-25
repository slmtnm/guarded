from dataclasses import dataclass
import dataclasses
from functools import reduce
from gclang.gen.GuardedVisitor import GuardedVisitor

import sympy as sp

from gclang.guarded_exception import GuardedException

from ..gen.GuardedParser import GuardedParser


def compose(*fns):
    return reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)

@dataclasses.dataclass
class Function:
    parameters: list[str]
    body: GuardedParser.OperatorListContext


class ReverseVisitor(GuardedVisitor):
    def __init__(self):
        self._functions = {}
        self._replacement_stack = []
        self._predicate_stack = []

        self._depth = 1
        self._claims = []
        self._replace = True

    def visitTrue(self, ctx):
        return sp.true

    def visitFalse(self, ctx):
        return sp.false

    def visitIdentifier(self, ctx: GuardedParser.IdentifierContext):
        identifier = sp.Symbol(ctx.getText())
        if self._replace and self._replacement_stack and identifier in self._replacement_stack[-1]:
            return sp.Symbol('local ' + str(self._replacement_stack[-1][identifier]))
        return identifier

    def visitNumber(self, ctx: GuardedParser.NumberContext):
        return sp.Number(ctx.getText())

    def visitUnarySub(self, ctx: GuardedParser.UnarySubContext):
        return -self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))

    def visitNegate(self, ctx: GuardedParser.NegateContext):
        return sp.Not(self.visit(ctx.getChild(0, GuardedParser.ExpressionContext)))

    def visitAnd(self, ctx: GuardedParser.AndContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return sp.And(left, right)

    def visitOr(self, ctx: GuardedParser.OrContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return sp.Or(left, right)

    def visitImpl(self, ctx: GuardedParser.ImplContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return sp.Or(sp.Not(left), right)

    def visitExprMacroCall(self, ctx: GuardedParser.ExprMacroCallContext):
        function_name = ctx.getToken(GuardedParser.ID, 0).getText()

        parameters_ctx = ctx.getChild(
            0, GuardedParser.ActualParametersContext)
        parameters = [self.visit(node) for node in parameters_ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext
        )]

        return sp.Function(function_name)(*parameters)

    def visitLogic(self, ctx: GuardedParser.LogicContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        return {
            ctx.LT(): lambda x, y: sp.Lt(x, y),
            ctx.LE(): lambda x, y: sp.Le(x, y),
            ctx.GT(): lambda x, y: sp.Gt(x, y),
            ctx.GE(): lambda x, y: sp.Ge(x, y),
            ctx.EQ(): lambda x, y: sp.Eq(x, y),
            ctx.NEQ(): lambda x, y: sp.Not(sp.Eq(x, y)),
        }[ctx.getChild(1)](left, right)

    def visitAddSub(self, ctx: GuardedParser.AddSubContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        return {
            ctx.ADD(): lambda x, y: sp.Add(x, y),
            ctx.SUB(): lambda x, y: sp.Add(x, sp.Mul(-1, y)),
        }[ctx.getChild(1)](left, right)

    def visitMulDiv(self, ctx: GuardedParser.MulDivContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        return {
            ctx.MUL(): lambda x, y: sp.Mul(x, y),
            ctx.DIV(): lambda x, y: sp.Mul(x, sp.Pow(y, -1)),
        }[ctx.getChild(1)](left, right)

    def visitAssignOperator(self, ctx: GuardedParser.AssignOperatorContext):
        var_names = list(map(str, ctx.getTokens(GuardedParser.ID)))
        var_values = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        old_condition = self._predicate_stack.pop()

        if ctx.getTokens(GuardedParser.LOCAL_VARIABLE):
            local_vars = map(compose(sp.Symbol, lambda v: 'local ' + v), var_names)
            new_condition = old_condition.xreplace(dict(zip(local_vars, var_values)))
        else:
            vars, local_vars = map(sp.Symbol, var_names), map(compose(sp.Symbol, lambda v: 'local ' + v), var_names)
            new_condition = old_condition.xreplace(
                dict(zip(local_vars, var_values)) | dict(zip(vars, var_values))
            )

        print('    ' * self._depth +
              f'{old_condition} --[assign {list(var_names)}:={var_values}]--> {new_condition}')

        self._predicate_stack.append(new_condition)

    def visitIfOperator(self, ctx: GuardedParser.AssignOperatorContext):
        command_list_ctx = ctx.getChild(0, GuardedParser.CommandListContext)
        commands = command_list_ctx.getTypedRuleContexts(
            GuardedParser.CommandContext)
        predicate = self._predicate_stack.pop()

        @dataclass
        class Command:
            fuse:      sp.Basic
            predicate: sp.Basic

        command_predicates: list[Command] = []
        for command in commands:
            fuse = self.visit(command.getChild(
                0, GuardedParser.ExpressionContext))
            body = command.getChild(0, GuardedParser.OperatorListContext)

            self._predicate_stack.append(predicate)
            self.visitOperatorList(body)
            new_predicate = self._predicate_stack.pop()
            command_predicates.append(
                Command(fuse=fuse, predicate=new_predicate))

        BB = reduce(
            sp.Or, [c.fuse for c in command_predicates], sp.false)
        R = reduce(
            sp.And, [sp.Implies(c.fuse, c.predicate) for c in command_predicates], sp.true)
        new_predicate = sp.And(BB, R)

        print('    ' * self._depth +
              f'{str(predicate)} --[if]--> {str(new_predicate)}')
        self._predicate_stack.append(new_predicate)

    def visitDoOperator(self, ctx: GuardedParser.DoOperatorContext):
        condition = ctx.getChild(0, GuardedParser.ConditionContext)
        if condition == None:
            raise GuardedException(ctx.start.line, "do..od operator without invariant in deriving mode")

        invariant = self.visitCondition(condition)
        old_predicate = self._predicate_stack.pop()
        self._predicate_stack.append(invariant)

        command_list_ctx = ctx.getChild(0, GuardedParser.CommandListContext)
        commands = command_list_ctx.getTypedRuleContexts(
            GuardedParser.CommandContext)

        R = reduce(
            sp.And,
            map(compose(sp.Not, self.visit), [c.getChild(
                0, GuardedParser.ExpressionContext) for c in commands]),
            invariant
        )

        claim_predicate = sp.Implies(
            R.simplify(), old_predicate)
        self._claims.append(str(claim_predicate))

    def visitOperatorList(self, ctx: GuardedParser.OperatorListContext):
        for operator in reversed(list(ctx.getChildren())):
            self.visitOperator(operator)

    def visitStart(self, ctx: GuardedParser.StartContext):
        for function_definition in ctx.getTypedRuleContexts(GuardedParser.MacroOperatorDefinitionContext):
            self.visit(function_definition)

        post_condition_ctx = ctx.getChild(0, GuardedParser.ConditionContext)
        if post_condition_ctx == None:
            raise GuardedException(ctx.start.line, 'Post-condition not found')

        post_condition = self.visitCondition(post_condition_ctx)
        self._predicate_stack.append(post_condition)

        print('Post-condition:', str(post_condition))
        self.visitChildren(ctx)
        pre_condition = sp.simplify(self._predicate_stack.pop())
        print('Pre-condition:', str(pre_condition.simplify()))

        self._claims and print(
            '\nPROVE manually, that following formulas are tauthologies:')
        for i in range(len(self._claims)):
            print(f'{i + 1}. {self._claims[i]}')

    def visitCondition(self, ctx: GuardedParser.ConditionContext):
        return self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))

    def visitInitialAssignments(self, ctx: GuardedParser.InitialAssignmentsContext):
        pass

    def visitMacroOperatorDefinition(self, ctx: GuardedParser.MacroOperatorDefinitionContext):
        function_name = ctx.getChild(0).getText()
        function_params = ctx.getChild(0, GuardedParser.FormalParametersContext)

        params = map(compose(sp.Symbol, str), function_params.getTokens(GuardedParser.ID))
        body  = ctx.getChild(0, GuardedParser.OperatorListContext)

        self._functions[function_name] = Function(list(params), body)

    def visitMacroCall(self, ctx: GuardedParser.MacroCallContext):
        function_name = ctx.getToken(GuardedParser.ID, 0).getText()
        params_ctx = ctx.getChild(0, GuardedParser.ActualParametersContext)
        function = self._functions[function_name]

        self._replace = False
        params = [self.visit(node) for node in params_ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        self._replace = True

        self._replacement_stack.append(dict(zip(function.parameters, params)))
        self.visitOperatorList(function.body)
        self._replacement_stack.pop()

    def visitBrackets(self, ctx: GuardedParser.BracketsContext):
        return self.visit(ctx.getTypedRuleContext(GuardedParser.ExpressionContext, 0))
