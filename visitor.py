from random import randint
from gen.SecureVisitor import SecureVisitor
from gen.SecureParser import SecureParser


class MySecureVisitor(SecureVisitor):
    def __init__(self):
        self.stack = []
        self.vars = {}

    def visitNumber(self, ctx: SecureParser.NumberContext):
        num = int(ctx.getText())
        self.stack.append(num)

    def visitIdentifier(self, ctx: SecureParser.IdentifierContext):
        value = self.vars[ctx.getText()]
        self.stack.append(value)

    def visitUnarySub(self, ctx: SecureParser.UnarySubContext):
        self.visitChildren(ctx)
        value = self.stack.pop()
        self.stack.append(-value)

    def visitAddSub(self, ctx: SecureParser.AddSubContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        right, left = self.stack.pop(), self.stack.pop()
        op = children[1]
        if op == ctx.ADD():
            self.stack.append(left + right)
        elif op == ctx.SUB():
            self.stack.append(left - right)
        else:
            raise Exception(f"Unexpected operation: {ctx.op}")

    def visitMulDiv(self, ctx: SecureParser.MulDivContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        right, left = self.stack.pop(), self.stack.pop()
        op = children[1]
        if op == ctx.MUL():
            self.stack.append(left * right)
        elif op == ctx.DIV():
            self.stack.append(left / right)
        else:
            raise Exception(f"Unexpected operation: {ctx.getText()}")

    def visitLogic(self, ctx:SecureParser.LogicContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        right, left = self.stack.pop(), self.stack.pop()
        op = children[1]
        if op == ctx.LT():
            self.stack.append(left < right)
        elif op == ctx.LE():
            self.stack.append(left <= right)
        elif op == ctx.GT():
            self.stack.append(left > right)
        elif op == ctx.GE():
            self.stack.append(left >= right)
        elif op == ctx.EQ():
            self.stack.append(left == right)
        elif op == ctx.NEQ():
            self.stack.append(left != right)
        else:
            raise Exception(f"Unexpected logical operation: {op}")

    def visitAssignOperator(self, ctx: SecureParser.AssignOperatorContext):
        self.visitChildren(ctx)

        children = list(ctx.getChildren())
        var_name = children[0].getText()
        var_value = self.stack.pop()

        self.vars[var_name] = var_value

    def visitCommand(self, ctx: SecureParser.CommandContext):
        children = list(ctx.getChildren())
        if not isinstance(children[0], SecureParser.LogicContext):
            raise Exception(f"Fuse of secure command must be valid logical expression")
        self.visitLogic(children[0])

        ctx.fuse = self.stack.pop()
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
        flag = True
        while flag:
            self.visitChildren(ctx)
            command_list = list(ctx.getChildren())[1]

            if len(command_list.true_commands) != 0:
                rand = randint(0, len(command_list.true_commands) - 1)
                self.visitOperatorList(command_list.true_commands[rand])
            else:
                flag = False
