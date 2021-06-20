from gclang.gen.GuardedVisitor import GuardedVisitor
from ..gen.GuardedParser import GuardedParser
import z3


class ForwardVisitor(GuardedVisitor):
    def __init__(self) -> None:
        super().__init__()
        self._vars = {}

    def visitTrue(self, ctx: GuardedParser.TrueContext):
        return True

    def visitFalse(self, ctx: GuardedParser.FalseContext):
        return False

    def visitAssignOperator(self, ctx: GuardedParser.AssignOperatorContext):
        var_name = ctx.getToken(GuardedParser.ID, 0).getText()
        value = self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))