from random import randint
from gen.SecureVisitor import SecureVisitor
from gen.SecureParser import SecureParser


class ExecutingVisitor(SecureVisitor):
    def __init__(self):
        self._stack = []

        self._state_var_names: list[str] = [] # names of state variables
        self._in_initial_state = False
        self.vars = {} # name -> value mapping of all variables, including state and temporary variables

    def visitNumber(self, ctx: SecureParser.NumberContext):
        num = int(ctx.getText())
        self._stack.append(num)

    def visitIdentifier(self, ctx: SecureParser.IdentifierContext):
        value = self.vars[ctx.getText()]
        self._stack.append(value)

    def visitTrue(self, ctx: SecureParser.TrueContext):
        self._stack.append(True)

    def visitFalse(self, ctx: SecureParser.FalseContext):
        self._stack.append(False)

    def visitUnarySub(self, ctx: SecureParser.UnarySubContext):
        self.visitChildren(ctx)
        value = self._stack.pop()
        self._stack.append(-value)

    def visitNegate(self, ctx: SecureParser.NegateContext):
        self.visitChildren(ctx)
        value = self._stack.pop()
        self._stack.append(not value)

    def visitAnd(self, ctx: SecureParser.AndContext):
        self.visitChildren(ctx)
        right, left = self._stack.pop(), self._stack.pop()
        self._stack.append(left and right)

    def visitOr(self, ctx: SecureParser.OrContext):
        self.visitChildren(ctx)
        right, left = self._stack.pop(), self._stack.pop()
        print(left, right)
        self._stack.append(left or right)

    def visitImpl(self, ctx: SecureParser.ImplContext):
        self.visitChildren(ctx)
        right, left = self._stack.pop(), self._stack.pop()
        return right or not left

    def visitEquiv(self, ctx: SecureParser.EquivContext):
        self.visitChildren(ctx)
        right, left = self._stack.pop(), self._stack.pop()
        return bool(left) == bool(right)

    def visitAddSub(self, ctx: SecureParser.AddSubContext):
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

    def visitMulDiv(self, ctx: SecureParser.MulDivContext):
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

    def visitLogic(self, ctx: SecureParser.LogicContext):
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

    def visitAssignOperator(self, ctx: SecureParser.AssignOperatorContext):
        self.visitChildren(ctx)

        children = list(ctx.getChildren())
        var_name = children[0].getText()
        var_value = self._stack.pop()

        self.vars[var_name] = var_value

        if self._in_initial_state:
            self._state_var_names.append(var_name)

    def visitCommand(self, ctx: SecureParser.CommandContext):
        children = list(ctx.getChildren())
        if isinstance(children[0], SecureParser.LogicContext):
            self.visitLogic(children[0])
        elif isinstance(children[0], SecureParser.TrueContext):
            self.visitTrue(children[0])
        elif isinstance(children[0], SecureParser.FalseContext):
            self.visitFalse(children[0])
        elif isinstance(children[0], SecureParser.AndContext):
            self.visitAnd(children[0])
        elif isinstance(children[0], SecureParser.OrContext):
            self.visitOr(children[0])
        elif isinstance(children[0], SecureParser.NegateContext):
            self.visitNegate(children[0])
        else:
            raise Exception(f"Fuse of secure command must be valid logical expression")

        ctx.fuse = self._stack.pop()
        ctx.command = children[2]

    def visitCommandList(self, ctx: SecureParser.CommandListContext):
        self.visitChildren(ctx)

        ctx.true_commands = []
        for child in ctx.getChildren():
            if isinstance(child, SecureParser.CommandContext) and child.fuse:
                ctx.true_commands.append(child.command)

    def visitIfOperator(self, ctx: SecureParser.IfOperatorContext):
        self.visitChildren(ctx)

        command_list = list(ctx.getChildren())[1]
        if len(command_list.true_commands) != 0:
            rand = randint(0, len(command_list.true_commands) - 1)
            self.visitOperatorList(command_list.true_commands[rand])

    def visitDoOperator(self, ctx: SecureParser.DoOperatorContext):
        while True:
            # recalc all fuses on each iteration
            self.visitChildren(ctx)

            command_list = list(ctx.getChildren())[1]
            if len(command_list.true_commands) != 0:
                rand = randint(0, len(command_list.true_commands) - 1)
                self.visitOperatorList(command_list.true_commands[rand])
            else:
                break

    def visitPostCondition(self, ctx: SecureParser.PostConditionContext):
        return # do not perform anything

    def visitInitialState(self, ctx: SecureParser.InitialStateContext):
        self._in_initial_state = True
        self.visitChildren(ctx)
        self._in_initial_state = False

    def getState(self) -> tuple[str, object]:
        for name in self._state_var_names:
            yield name, self.vars[name]
