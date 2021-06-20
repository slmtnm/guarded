from gclang.gen.GuardedParser import GuardedParser
from gclang.gen.GuardedVisitor import GuardedVisitor
from dataclasses import InitVar, dataclass

@dataclass
class MacroOperator:
    name: str
    parameters: tuple[str]
    body: GuardedParser.OperatorListContext

@dataclass
class MacroExpression:
    name: str
    parameters: tuple[str]
    body: GuardedParser.ExpressionContext

class MacroVisitor(GuardedVisitor):
    def __init__(self) -> None:
        super().__init__()
        self._replacement_stack = []

    def _get_vars(self):
        pass

    def _set_vars(self, vars):
        pass

    def visitActualParameters(self, ctx: GuardedParser.ActualParametersContext):
        return [self.visit(node) for node in ctx.getTypedRuleContexts(GuardedParser.ExpressionContext)]

    def visitExprMacroCall(self, ctx: GuardedParser.ExprMacroCallContext):
        macro_name = ctx.getToken(GuardedParser.ID, 0).getText()
        macro = self._get_vars()[macro_name]
        assert isinstance(macro, MacroExpression)

        parameters = self.visitActualParameters(ctx.getChild(0, GuardedParser.ActualParametersContext))
        assert len(macro.parameters) == len(parameters)

        vars = self._get_vars()
        snap = dict(vars)

        vars |= dict(zip(macro.parameters, parameters))
        result = self.visit(macro.body)
        self._set_vars(snap)

        return result

    def visitMacroExpressionDefinition(self, ctx: GuardedParser.MacroExpressionDefinitionContext):
        vars = self._get_vars()

        macro_name = ctx.getChild(0).getText()
        parameters_ctx = ctx.getChild(0, GuardedParser.FormalParametersContext)
        parameters = tuple(map(str, parameters_ctx.getTokens(GuardedParser.ID)))
        body = ctx.getChild(0, GuardedParser.ExpressionContext)

        vars[macro_name] = MacroExpression(macro_name, parameters, body)