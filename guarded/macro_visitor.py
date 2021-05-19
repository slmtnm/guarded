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
        children = list(ctx.getChildren())
        definition = list(children[0].getChildren())
        function_name = definition[0].getText()
        parameters = [param for param in definition[2:-1]]
        body = children[2]

        # TODO: check if all external identifiers in body are function parameters

        self.functions[function_name] = Function(parameters, body)

    def visitFunctionCall(self, ctx: GuardedParser.FunctionCallContext):
        children = list(ctx.getChildren())
        call = list(children[0].getChildren())
        function_name = call[0].getText()
        function = self.functions[function_name]

        actual_parameters = [param for param in call[2:-1]]
        assert len(actual_parameters) == len(function.parameters), \
            f"Formal and actual parameters length mismatch for function '{function_name}'"

        replacement = dict(zip(function.parameters, actual_parameters))
        self.replacementStack.append(replacement)
        self.visitOperatorList(function.body)
        self.replacementStack.pop()
