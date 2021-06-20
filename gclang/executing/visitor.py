import dataclasses
from gclang.gen.GuardedLexer import GuardedLexer
from gclang.executing.macro import MacroVisitor
from gclang.executing.array import ArrayVisitor
from gclang.gen.GuardedVisitor import GuardedVisitor
from random import choice

from gclang.guarded_exception import GuardedException

from ..gen.GuardedParser import GuardedParser

@dataclasses.dataclass
class Function:
    parameters: list[str]
    body: GuardedParser.OperatorListContext

class Visitor(ArrayVisitor, MacroVisitor):
    def __init__(self):
        super(ArrayVisitor, self).__init__()
        super(MacroVisitor, self).__init__()

        self._functions = {}
        self._vars = {}

    def _get_var(self, var_name):
        if var_name in self._vars:
            return self._vars[var_name]
        elif var_name in self._replacement_stack[-1]:
            return self._replacement_stack[-1][var_name]
        return None

    def _get_vars(self):
        return self._vars

    def _set_vars(self, vars):
        self._vars = vars

    def visitSkipOperator(self, ctx: GuardedParser.SkipOperatorContext):
        pass

    def visitAbortOperator(self, ctx: GuardedParser.AbortOperatorContext):
        raise GuardedException(ctx.start.line, 'Abort operator')

    def visitPrintOperator(self, ctx: GuardedParser.PrintOperatorContext):
        value = self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))
        print(value)

    def visitNumber(self, ctx: GuardedParser.NumberContext):
        return float(ctx.getText())

    def visitIdentifier(self, ctx: GuardedParser.IdentifierContext):
        identifier = ctx.getText()

        if identifier in self._vars:
            return self._vars[identifier]

        if self._replacement_stack:
            replacement = self._replacement_stack[-1]
            if identifier in replacement:
                return replacement[identifier]

        raise GuardedException(ctx.start.line, "Undefined identifier " + identifier)

    def visitTrue(self, ctx: GuardedParser.TrueContext):
        return True

    def visitFalse(self, ctx: GuardedParser.FalseContext):
        return False

    def visitUnarySub(self, ctx: GuardedParser.UnarySubContext):
        return -self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))

    def visitNegate(self, ctx: GuardedParser.NegateContext):
        return not self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))

    def visitAnd(self, ctx: GuardedParser.AndContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return left and right

    def visitOr(self, ctx: GuardedParser.OrContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return left or right

    def visitImpl(self, ctx: GuardedParser.ImplContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return not left or right

    def visitEquiv(self, ctx: GuardedParser.EquivContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        return left == right

    def visitAddSub(self, ctx: GuardedParser.AddSubContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        return {
            ctx.ADD(): lambda x, y: x + y,
            ctx.SUB(): lambda x, y: x - y
        }[ctx.getChild(1)](left, right)

    def visitMulDiv(self, ctx: GuardedParser.MulDivContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        return {
            ctx.MUL(): lambda x, y: x * y,
            ctx.DIV(): lambda x, y: x / y
        }[ctx.getChild(1)](left, right)

    def visitLogic(self, ctx: GuardedParser.LogicContext):
        left, right = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        return {
            ctx.LT(): lambda x, y: x < y,
            ctx.LE(): lambda x, y: x <= y,
            ctx.GT(): lambda x, y: x > y,
            ctx.GE(): lambda x, y: x >= y,
            ctx.EQ(): lambda x, y: x == y,
            ctx.NEQ(): lambda x, y: x != y,
        }[ctx.getChild(1)](left, right)

    def visitAssignOperator(self, ctx: GuardedParser.AssignOperatorContext):
        var_names = map(str, ctx.getTokens(GuardedParser.ID))
        var_values = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        if ctx.getTokens(GuardedParser.LOCAL_VARIABLE):
            if not self._replacement_stack:
                raise GuardedException(line=ctx.start.line, message='Private variable outside any function')
            self._replacement_stack[-1] |= dict(zip(var_names, var_values))
        else:
            self._vars |= dict(zip(var_names, var_values))

    def visitCommand(self, ctx: GuardedParser.CommandContext):
        fuse = self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))
        command = ctx.getChild(0, GuardedParser.OperatorListContext)

        return fuse, command

    def visitCommandList(self, ctx: GuardedParser.CommandListContext):
        potential = []
        for command in ctx.getTypedRuleContexts(GuardedParser.CommandContext):
            fuse, body = self.visit(command)
            if fuse:
                potential.append(body)

        if not potential:
            return None
        else:
            return choice(potential)

    def visitIfOperator(self, ctx: GuardedParser.IfOperatorContext):
        body = self.visit(ctx.getChild(0, GuardedParser.CommandListContext))
        if not body:
            raise GuardedException(ctx.start.line, "No truthy guarded command in if..fi operator")
        else:
            self.visitOperatorList(body)

    def visitDoOperator(self, ctx: GuardedParser.DoOperatorContext):
        while True:
            body = self.visit(ctx.getChild(
                0, GuardedParser.CommandListContext))
            if not body:
                break
            self.visitOperatorList(body)

    def visitStart(self, ctx: GuardedParser.StartContext):
        if ctx.getChildCount() == 1 and isinstance(ctx.getChild(0), GuardedParser.ExpressionContext):
            return {'ans': self.visit(ctx.getChild(0))}

        for function_definition in ctx.getTypedRuleContexts(GuardedParser.MacroOperatorDefinitionContext):
            self.visit(function_definition)
        self.visitChildren(ctx)
        return self._vars

    def visitMacroCall(self, ctx: GuardedParser.MacroCallContext):
        function_name = ctx.getToken(GuardedParser.ID, 0).getText()
        params_ctx = ctx.getChild(0, GuardedParser.ActualParametersContext)
        function = self._functions[function_name]

        params = [self.visit(node) for node in params_ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        replacement = dict(zip(function.parameters, params))
        self._replacement_stack.append(replacement)
        old_vars = self._vars
        self._vars = {}
        self.visitOperatorList(function.body)
        self._vars = old_vars | self._vars
        self._replacement_stack.pop()

    def visitCondition(self, ctx: GuardedParser.ConditionContext):
        pass

    def visitMacroOperatorDefinition(self, ctx: GuardedParser.MacroOperatorDefinitionContext):
        function_name = ctx.getChild(0).getText()
        function_params = ctx.getChild(0, GuardedParser.FormalParametersContext)

        params = map(str, function_params.getTokens(GuardedParser.ID))
        body  = ctx.getChild(0, GuardedParser.OperatorListContext)

        self._functions[function_name] = Function(list(params), body)

    def visitBrackets(self, ctx: GuardedParser.BracketsContext):
        return self.visit(ctx.getTypedRuleContext(GuardedParser.ExpressionContext, 0))