from random import randint
from gen.GuardedVisitor import GuardedVisitor
from gen.GuardedParser import GuardedParser


class ExecutingVisitor(GuardedVisitor):
    def __init__(self):
        self._stack = []

        self.vars = {} # name -> value mapping of all variables

    def visitNumber(self, ctx: GuardedParser.NumberContext):
        num = float(ctx.getText())
        self._stack.append(num)

    def visitIdentifier(self, ctx: GuardedParser.IdentifierContext):
        value = self.vars[ctx.getText()]
        self._stack.append(value)

    def visitTrue(self, ctx: GuardedParser.TrueContext):
        self._stack.append(True)

    def visitFalse(self, ctx: GuardedParser.FalseContext):
        self._stack.append(False)

    def visitUnarySub(self, ctx: GuardedParser.UnarySubContext):
        self.visitChildren(ctx)
        value = self._stack.pop()
        self._stack.append(-value)

    def visitNegate(self, ctx: GuardedParser.NegateContext):
        self.visitChildren(ctx)
        value = self._stack.pop()
        self._stack.append(not value)

    def visitAnd(self, ctx: GuardedParser.AndContext):
        self.visitChildren(ctx)
        right, left = self._stack.pop(), self._stack.pop()
        self._stack.append(left and right)

    def visitOr(self, ctx: GuardedParser.OrContext):
        self.visitChildren(ctx)
        right, left = self._stack.pop(), self._stack.pop()
        print(left, right)
        self._stack.append(left or right)

    def visitImpl(self, ctx: GuardedParser.ImplContext):
        self.visitChildren(ctx)
        right, left = self._stack.pop(), self._stack.pop()
        return right or not left

    def visitEquiv(self, ctx: GuardedParser.EquivContext):
        self.visitChildren(ctx)
        right, left = self._stack.pop(), self._stack.pop()
        return bool(left) == bool(right)

    def visitAddSub(self, ctx: GuardedParser.AddSubContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        right, left = self._stack.pop(), self._stack.pop()
        op = children[1]
        if op == ctx.ADD():
            self._stack.append(left + right)
        elif op == ctx.SUB():
            self._stack.append(left - right)
        else:
            raise Exception(f"Unexpected operation: {ctx.op}")

    def visitMulDiv(self, ctx: GuardedParser.MulDivContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        right, left = self._stack.pop(), self._stack.pop()
        op = children[1]
        if op == ctx.MUL():
            self._stack.append(left * right)
        elif op == ctx.DIV():
            self._stack.append(left / right)
        else:
            raise Exception(f"Unexpected operation: {ctx.getText()}")

    def visitLogic(self, ctx: GuardedParser.LogicContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        right, left = self._stack.pop(), self._stack.pop()
        op = children[1]
        if op == ctx.LT():
            self._stack.append(left < right)
        elif op == ctx.LE():
            self._stack.append(left <= right)
        elif op == ctx.GT():
            self._stack.append(left > right)
        elif op == ctx.GE():
            self._stack.append(left >= right)
        elif op == ctx.EQ():
            self._stack.append(left == right)
        elif op == ctx.NEQ():
            self._stack.append(left != right)
        else:
            raise Exception(f"Unexpected logical operation: {op}")

    def visitAssignOperator(self, ctx: GuardedParser.AssignOperatorContext):
        self.visitChildren(ctx)

        children = list(ctx.getChildren())
        var_name = children[0].getText()
        var_value = self._stack.pop()

        self.vars[var_name] = var_value

    def visitCommand(self, ctx: GuardedParser.CommandContext):
        children = list(ctx.getChildren())
        if isinstance(children[0], GuardedParser.LogicContext):
            self.visitLogic(children[0])
        elif isinstance(children[0], GuardedParser.TrueContext):
            self.visitTrue(children[0])
        elif isinstance(children[0], GuardedParser.FalseContext):
            self.visitFalse(children[0])
        elif isinstance(children[0], GuardedParser.AndContext):
            self.visitAnd(children[0])
        elif isinstance(children[0], GuardedParser.OrContext):
            self.visitOr(children[0])
        elif isinstance(children[0], GuardedParser.NegateContext):
            self.visitNegate(children[0])
        else:
            raise Exception(f"Fuse of Guarded command must be valid logical expression")

        ctx.fuse = self._stack.pop()
        ctx.command = children[2]

    def visitCommandList(self, ctx: GuardedParser.CommandListContext):
        self.visitChildren(ctx)

        ctx.true_commands = []
        for child in ctx.getChildren():
            if isinstance(child, GuardedParser.CommandContext) and child.fuse:
                ctx.true_commands.append(child.command)

    def visitIfOperator(self, ctx: GuardedParser.IfOperatorContext):
        self.visitChildren(ctx)

        command_list = list(ctx.getChildren())[1]
        if len(command_list.true_commands) != 0:
            rand = randint(0, len(command_list.true_commands) - 1)
            self.visitOperatorList(command_list.true_commands[rand])


    def visitDoOperator(self, ctx: GuardedParser.DoOperatorContext):
        while True:
            # recalc all fuses on each iteration
            self.visitChildren(ctx)

            command_list = next(c for c in ctx.getChildren() if isinstance(c, GuardedParser.CommandListContext))
            if len(command_list.true_commands) != 0:
                rand = randint(0, len(command_list.true_commands) - 1)
                self.visitOperatorList(command_list.true_commands[rand])
            else:
                break

    def visitCondition(self, ctx: GuardedParser.ConditionContext):
        return # do not perform anything