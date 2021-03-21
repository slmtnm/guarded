from gen.SecureVisitor import SecureVisitor
from gen.SecureParser import SecureParser
from antlr4.tree.Tree import TerminalNode

from itertools import islice


class DerivingVisitor(SecureVisitor):
    def __init__(self):
        self._stack: list[str] = []
        self._state_var_names: list[str] = []

    def visitAssignOperator(self, ctx: SecureParser.AssignOperatorContext):
        children = list(ctx.getChildren())
        current_condition: str = self._stack.pop()
        self._stack.append(current_condition.replace(children[0].getText(), children[2].getText()))

    def visitIfOperator(self, ctx: SecureParser.AssignOperatorContext):
        children = list(ctx.getChildren())
        commandList = filter(lambda c: isinstance(c, SecureParser.CommandContext),
            children[1].getChildren())
        current_predicate = self._stack.pop()

        fuses = []
        operator_list_predicates = []
        for command in commandList:
            command_children = list(command.getChildren())
            fuse: str = command_children[0].getText()
            fuses.append(fuse)

            operator_list: SecureParser.OperatorListContext = command_children[2]
            self._stack.append(current_predicate)
            self.visitOperatorList(operator_list)
            predicate = self._stack.pop()

            operator_list_predicates.append((fuse, predicate))
        fuses_str = ' | '.join(fuses)
        fuses_str = f'({fuses_str})'
        pred_str = ' & '.join(f'({fuse} >> {pred})' for fuse, pred in operator_list_predicates)
        pred_str = f'({pred_str})'

        self._stack.append(f'{fuses_str} & {pred_str}')


    def visitOperatorList(self, ctx: SecureParser.OperatorListContext):
        for operator in reversed(list(ctx.getChildren())):
            self.visitOperator(operator)


    def visitStart(self, ctx: SecureParser.StartContext):
        try:
            post_condition_ctx: SecureParser.PostConditionContext = next(c for c in ctx.getChildren()
                if isinstance(c, SecureParser.PostConditionContext))
        except StopIteration as err:
            raise Exception('Post-condition not found')

        post_condition_str = list(post_condition_ctx.getChildren())[1].getText()
        self._stack.append(post_condition_str)

        self.visitChildren(ctx)

    def visitInitialState(self, ctx: SecureParser.InitialStateContext):
        children = list(ctx.getChildren())[1:-1]

        for ao in children:
            if not isinstance(ao, SecureParser.AssignOperatorContext):
                continue

            self._state_var_names.append(next(ao.getChildren()).getText())

    def getStateVars(self):
        yield from self._state_var_names

    def getPreCondition(self):
        assert len(self._stack) == 1

        return self._stack.pop()