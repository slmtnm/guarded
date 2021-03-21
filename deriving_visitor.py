from gen.SecureVisitor import SecureVisitor
from gen.SecureParser import SecureParser
from antlr4.tree.Tree import TerminalNode
import sympy as sp


class DerivingVisitor(SecureVisitor):
    def __init__(self):
        self._expr_stack = []
        self._predicate_stack = []
        self._state_var_names: list[str] = []

        self._depth = 0

    def visitExpression(self, ctx):
        if isinstance(ctx, SecureParser.TrueContext):
            self.visitTrue(ctx)
        elif isinstance(ctx, SecureParser.FalseContext):
            self.visitFalse(ctx)
        elif isinstance(ctx, SecureParser.AndContext):
            self.visitAnd(ctx)
        elif isinstance(ctx, SecureParser.OrContext):
            self.visitOr(ctx)
        elif isinstance(ctx, SecureParser.ImplContext):
            self.visitImpl(ctx)
        elif isinstance(ctx, SecureParser.IdentifierContext):
            self.visitIdentifier(ctx)
        elif isinstance(ctx, SecureParser.LogicContext):
            self.visitLogic(ctx)
        elif isinstance(ctx, SecureParser.MulDivContext):
            self.visitMulDiv(ctx)
        elif isinstance(ctx, SecureParser.AddSubContext):
            self.visitAddSub(ctx)
        elif isinstance(ctx, SecureParser.BracketsContext):
            self.visitBrackets(ctx)
        elif isinstance(ctx, SecureParser.NegateContext):
            self.visitNegate(ctx)
        elif isinstance(ctx, SecureParser.NumberContext):
            self.visitNumber(ctx)
        elif isinstance(ctx, SecureParser.UnarySubContext):
            self.visitUnarySub(ctx)
    
    def visitTrue(self, ctx):
        self._expr_stack.append(sp.true)
    def visitFalse(self, ctx):
        self._expr_stack.append(sp.false)
    def visitIdentifier(self, ctx: SecureParser.IdentifierContext):
        var_name = ctx.getText()
        self._expr_stack.append(sp.Symbol(var_name))
    def visitNumber(self, ctx: SecureParser.NumberContext):
        num = int(ctx.getText())
        self._expr_stack.append(num)
    def visitUnarySub(self, ctx: SecureParser.UnarySubContext):
        self.visitChildren(ctx)
        value = self._expr_stack.pop()
        self._expr_stack.append(-value)
    def visitNegate(self, ctx: SecureParser.NegateContext):
        self.visitChildren(ctx)
        value = self._expr_stack.pop()
        self._expr_stack.append(sp.Not(value))
    def visitAnd(self, ctx: SecureParser.AndContext):
        self.visitChildren(ctx)
        right, left = self._expr_stack.pop(), self._expr_stack.pop()
        self._expr_stack.append(sp.And(left, right))
    def visitOr(self, ctx: SecureParser.OrContext):
        self.visitChildren(ctx)
        right, left = self._expr_stack.pop(), self._expr_stack.pop()
        self._expr_stack.append(sp.Or(left, right))
    def visitImpl(self, ctx: SecureParser.ImplContext):
        self.visitChildren(ctx)
        right, left = self._expr_stack.pop(), self._expr_stack.pop()
        self._expr_stack.append(sp.Implies(left, right))
    def visitLogic(self, ctx: SecureParser.LogicContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        right, left = self._expr_stack.pop(), self._expr_stack.pop()
        op = children[1]
        if op == ctx.LT():
            self._expr_stack.append(sp.Lt(left, right))
        elif op == ctx.LE():
            self._expr_stack.append(sp.Le(left, right))
        elif op == ctx.GT():
            self._expr_stack.append(sp.Gt(left, right))
        elif op == ctx.GE():
            self._expr_stack.append(sp.Ge(left, right))
        elif op == ctx.EQ():
            self._expr_stack.append(sp.Eq(left, right))
        elif op == ctx.NEQ():
            self._expr_stack.append(sp.Not(sp.Eq(left, right)))
        else:
            raise Exception(f"Unexpected logical operation: {op}")
    def visitAddSub(self, ctx: SecureParser.AddSubContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        right, left = self._expr_stack.pop(), self._expr_stack.pop()
        op = children[1]
        if op == ctx.ADD():
            self._expr_stack.append(sp.Add(left, right))
        elif op == ctx.SUB():
            self._expr_stack.append(sp.Add(left, sp.Mul(-1, right)))
        else:
            raise Exception(f"Unexpected operation: {ctx.op}")
    def visitMulDiv(self, ctx: SecureParser.MulDivContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        right, left = self._expr_stack.pop(), self._expr_stack.pop()
        op = children[1]
        if op == ctx.MUL():
            self._expr_stack.append(sp.Mul(left, right))
        elif op == ctx.DIV():
            self._expr_stack.append(sp.Mul(left, sp.Pow(right, -1)))
        else:
            raise Exception(f"Unexpected operation: {ctx.getText()}")

    def visitAssignOperator(self, ctx: SecureParser.AssignOperatorContext):
        self.visitChildren(ctx)
        children = list(ctx.getChildren())

        var_name = children[0].getText()
        var_value = self._expr_stack.pop()

        old_condition = self._predicate_stack.pop()
        new_condition = old_condition.xreplace({sp.Symbol(var_name): var_value})

        print('    ' * self._depth + f'{old_condition} --[assign {var_name}:={var_value}]--> {new_condition}')
        
        self._predicate_stack.append(new_condition)

    def visitIfOperator(self, ctx: SecureParser.AssignOperatorContext):
        children = list(ctx.getChildren())
        commandList = filter(lambda c: isinstance(c, SecureParser.CommandContext),
            children[1].getChildren())
        current_predicate = self._predicate_stack.pop()

        operator_list_predicates = []
        for command in commandList:
            command_children = list(command.getChildren())
            self.visitExpression(command_children[0])
            fuse = self._expr_stack.pop() # take fuse predicate

            operator_list: SecureParser.OperatorListContext = command_children[2]
            self._predicate_stack.append(current_predicate)
            self._depth += 1
            self.visitOperatorList(operator_list)
            self._depth -= 1
            predicate = self._predicate_stack.pop()

            operator_list_predicates.append((fuse, predicate))
        
        fuse_predicate = sp.false
        operator_list_predicate = sp.true
        for fuse, operator_list in operator_list_predicates:
            fuse_predicate = sp.Or(fuse_predicate, fuse)
            operator_list_predicate = sp.And(operator_list_predicate, sp.Implies(fuse, operator_list))
        
        new_predicate = sp.And(fuse_predicate, operator_list_predicate)
        print('    ' * self._depth + f'{str(current_predicate)} --[if]--> {str(new_predicate)}')
        self._predicate_stack.append(new_predicate)


    def visitOperatorList(self, ctx: SecureParser.OperatorListContext):
        for operator in reversed(list(ctx.getChildren())):
            self.visitOperator(operator)

    def visitStart(self, ctx: SecureParser.StartContext):
        try:
            post_condition_ctx: SecureParser.PostConditionContext = next(c for c in ctx.getChildren()
                if isinstance(c, SecureParser.PostConditionContext))
        except StopIteration:
            raise Exception('Post-condition not found')

        self.visitPostCondition(post_condition_ctx)
        post_condition = self._expr_stack.pop()

        # post_condition_str = list(post_condition_ctx.getChildren())[1].getText()
        # post_condition = sp.parse_expr(post_condition_str)
        self._predicate_stack.append(post_condition)

        print('Post-condition:', str(post_condition))
        self.visitChildren(ctx)
        pre_condition = sp.simplify(self._predicate_stack.pop())
        print('Pre-condition:', str(pre_condition.simplify()))

    def visitInitialState(self, ctx: SecureParser.InitialStateContext):
        children = list(ctx.getChildren())[1:-1]

        for ao in children:
            if not isinstance(ao, SecureParser.AssignOperatorContext):
                continue

            self._state_var_names.append(next(ao.getChildren()).getText())

    def getStateVars(self):
        yield from self._state_var_names