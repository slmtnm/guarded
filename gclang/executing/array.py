from gclang.gen.GuardedParser import GuardedParser
from gclang.gen.GuardedVisitor import GuardedVisitor
from dataclasses import dataclass


@dataclass
class Array:
    lower_bound: int
    data: list[object]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i - self.lower_bound]

    def __setitem__(self, i, v):
        self.data[i - self.lower_bound] = v

    def __repr__(self) -> str:
        result = f'[{self.lower_bound}| '
        if len(self.data) == 0:
            result += ']'
        elif len(self.data) == 1:
            result += f'{self.data[0]}]'
        else:
            for i in range(len(self.data) - 1):
                result += f'{self.data[i]}, '
            result += f'{self.data[-1]}]'
        return result

    @property
    def upper_bound(self) -> int:
        return self.lower_bound + len(self.data) - 1

class ArrayVisitor(GuardedVisitor):
    def __init__(self) -> None:
        super().__init__()

    def _get_vars(self):
        pass

    def _get_var(self, var_name):
        pass

    def visitArrayLiteral(self, ctx: GuardedParser.ArrayLiteralContext):
        all = [self.visit(node) for node in ctx.getTypedRuleContexts(GuardedParser.ExpressionContext)]

        if ctx.getTokens(GuardedParser.LOWER_BOUND_DELIMITER):
            lower_bound, *data = all
        else:
            lower_bound = 0
            data = all

        return Array(int(lower_bound), data)

    def visitArraySet(self, ctx: GuardedParser.ArraySetContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)
        index, value = [self.visit(node) for node in ctx.getTypedRuleContexts(
            GuardedParser.ExpressionContext)]
        index = int(index)
        assert array.lower_bound <= index <= array.lower_bound + len(array) - 1
        array[index] = value

    def visitArrayDelUp(self, ctx: GuardedParser.ArrayDelUpContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array) and len(array) > 0
        array.data.pop()

    def visitArrayDelDown(self, ctx: GuardedParser.ArrayDelDownContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array) and len(array) > 0
        del array.data[0]
        array.lower_bound += 1

    def visitArraySize(self, ctx: GuardedParser.ArraySizeContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)

        return len(array)

    def visitArrayLowerBound(self, ctx: GuardedParser.ArrayLowerBoundContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)

        return array.lower_bound

    def visitArrayUpperBound(self, ctx: GuardedParser.ArrayUpperBoundContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)

        return array.upper_bound

    def visitArrayElement(self, ctx: GuardedParser.ArrayElementContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)

        index = int(self.visit(ctx.getChild(0, GuardedParser.ExpressionContext)))
        return array[index]

    def visitArrayLowerElement(self, ctx: GuardedParser.ArrayLowerElementContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)

        return array[array.lower_bound]

    def visitArrayUpperElement(self, ctx: GuardedParser.ArrayUpperElementContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)

        return array[array.upper_bound]

    def visitArrayShift(self, ctx: GuardedParser.ArrayShiftContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)
        value = self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))
        array.lower_bound += value

    def visitArrayPushUp(self, ctx: GuardedParser.ArrayPushUpContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)
        value = self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))
        array.data.append(value)

    def visitArrayPushDown(self, ctx: GuardedParser.ArrayPushDownContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)
        value = self.visit(ctx.getChild(0, GuardedParser.ExpressionContext))
        array.data.insert(0, value)

    def visitArrayPopUp(self, ctx: GuardedParser.ArrayPopUpContext):
        var_name, array_name = map(str, ctx.getTokens(GuardedParser.ID))
        array = self._get_var(array_name)
        assert isinstance(array, Array) and len(array) > 0
        self._get_vars()[var_name] = array.data.pop()

    def visitArrayPopDown(self, ctx: GuardedParser.ArrayPopDownContext):
        var_name, array_name = map(str, ctx.getTokens(GuardedParser.ID))
        array = self._get_var(array_name)
        assert isinstance(array, Array) and len(array) > 0
        self._get_vars()[var_name] = array.data.pop(0)

    def visitArraySwap(self, ctx: GuardedParser.ArraySwapContext):
        array = self._get_var(ctx.getToken(GuardedParser.ID, 0).getText())
        assert isinstance(array, Array)

        i, j = [int(self.visit(node)) for node in ctx.getTypedRuleContexts(GuardedParser.ExpressionContext)]
        assert array.lower_bound <= i <= array.upper_bound and array.lower_bound <= j <= array.upper_bound

        array[i], array[j] = array[j], array[i]