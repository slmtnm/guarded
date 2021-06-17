from random import choice

from .gen.GuardedParser import GuardedParser
from .macro_visitor import MacroVisitor


class ExecutingVisitor(MacroVisitor):
    def __init__(self):
        super(ExecutingVisitor, self).__init__()
        self.vars = {}  # name -> value mapping of all variables

    def visitNumber(self, ctx: GuardedParser.NumberContext):
        return float(ctx.getText())

    def visitIdentifier(self, ctx: GuardedParser.IdentifierContext):
        identifier = ctx.getText()

        if identifier in self.vars:
            return self.vars[identifier]

        if self.replacementStack:
            replacement = self.replacementStack[-1]
            if identifier in replacement:
                return replacement[identifier]

        raise AssertionError("Undefined identifier " + identifier)

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
        self.vars |= dict(zip(var_names, var_values))

    def visitExprFnCall(self, ctx: GuardedParser.ExprFnCallContext):
        raise Exception("Macro function call in expression")

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
            raise Exception("No truthy guarded command in if..fi operator")
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
        for function_definition in ctx.getTypedRuleContexts(GuardedParser.FunctionDefinitionContext):
            self.visit(function_definition)
        self.visitChildren(ctx)
        return self.vars

    def visitFunctionCall(self, ctx: GuardedParser.FunctionCallContext):
        function_name = ctx.getToken(GuardedParser.ID, 0).getText()
        params_ctx = ctx.getChild(0, GuardedParser.ActualParametersContext)
        function = self.functions[function_name]

        params = [self.visit(node) for node in params_ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]

        replacement = dict(zip(function.parameters, params))
        self.replacementStack.append(replacement)
        old_vars = self.vars
        self.vars = {}
        self.visitOperatorList(function.body)
        self.vars = old_vars | self.vars
        self.replacementStack.pop()

    def visitCondition(self, ctx: GuardedParser.ConditionContext):
        pass
