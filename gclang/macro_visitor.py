import dataclasses

from .gen.GuardedVisitor import GuardedVisitor
from .gen.GuardedParser import GuardedParser

@dataclasses.dataclass
class Function:
    parameters: list[str]
    body: GuardedParser.OperatorListContext


class MacroVisitor(GuardedVisitor):

    def __init__(self):
        self.functions = {}
        self.replacementStack = []

    def visitFunctionDefinition(self, ctx: GuardedParser.FunctionDefinitionContext):
        function_name = ctx.getChild(0).getText()
        function_params = ctx.getChild(0, GuardedParser.FormalParametersContext)
        
        params = map(str, function_params.getTokens(GuardedParser.ID))
        body  = ctx.getChild(0, GuardedParser.OperatorListContext)

        self.functions[function_name] = Function(list(params), body)