# Generated from Secure.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("`\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\5\2\"\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\63\n\2\f\2\16\2")
        buf.write("\66\13\2\3\3\3\3\3\3\3\4\3\4\3\4\7\4>\n\4\f\4\16\4A\13")
        buf.write("\4\3\5\3\5\3\5\5\5F\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7")
        buf.write("\7O\n\7\f\7\16\7R\13\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\2\3\2\13\2\4\6\b\n\f\16\20\22\2\5")
        buf.write("\3\2\22\23\3\2\24\25\3\2\26\33\2e\2!\3\2\2\2\4\67\3\2")
        buf.write("\2\2\6:\3\2\2\2\bE\3\2\2\2\nG\3\2\2\2\fK\3\2\2\2\16S\3")
        buf.write("\2\2\2\20W\3\2\2\2\22[\3\2\2\2\24\25\b\2\1\2\25\26\7\25")
        buf.write("\2\2\26\"\5\2\2\16\27\30\7\36\2\2\30\"\5\2\2\r\31\32\7")
        buf.write("\3\2\2\32\33\5\2\2\2\33\34\7\4\2\2\34\"\3\2\2\2\35\"\7")
        buf.write("\16\2\2\36\"\7\21\2\2\37\"\7\17\2\2 \"\7\20\2\2!\24\3")
        buf.write("\2\2\2!\27\3\2\2\2!\31\3\2\2\2!\35\3\2\2\2!\36\3\2\2\2")
        buf.write("!\37\3\2\2\2! \3\2\2\2\"\64\3\2\2\2#$\f\13\2\2$%\t\2\2")
        buf.write("\2%\63\5\2\2\f&\'\f\n\2\2\'(\t\3\2\2(\63\5\2\2\13)*\f")
        buf.write("\t\2\2*+\t\4\2\2+\63\5\2\2\n,-\f\b\2\2-.\7\34\2\2.\63")
        buf.write("\5\2\2\t/\60\f\7\2\2\60\61\7\35\2\2\61\63\5\2\2\b\62#")
        buf.write("\3\2\2\2\62&\3\2\2\2\62)\3\2\2\2\62,\3\2\2\2\62/\3\2\2")
        buf.write("\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\3\3\2")
        buf.write("\2\2\66\64\3\2\2\2\678\5\6\4\289\7\2\2\39\5\3\2\2\2:?")
        buf.write("\5\b\5\2;<\7\f\2\2<>\5\b\5\2=;\3\2\2\2>A\3\2\2\2?=\3\2")
        buf.write("\2\2?@\3\2\2\2@\7\3\2\2\2A?\3\2\2\2BF\5\n\6\2CF\5\20\t")
        buf.write("\2DF\5\22\n\2EB\3\2\2\2EC\3\2\2\2ED\3\2\2\2F\t\3\2\2\2")
        buf.write("GH\7\21\2\2HI\7\5\2\2IJ\5\2\2\2J\13\3\2\2\2KP\5\16\b\2")
        buf.write("LM\7\6\2\2MO\5\16\b\2NL\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ")
        buf.write("\3\2\2\2Q\r\3\2\2\2RP\3\2\2\2ST\5\2\2\2TU\7\7\2\2UV\5")
        buf.write("\6\4\2V\17\3\2\2\2WX\7\b\2\2XY\5\f\7\2YZ\7\t\2\2Z\21\3")
        buf.write("\2\2\2[\\\7\n\2\2\\]\5\f\7\2]^\7\13\2\2^\23\3\2\2\2\b")
        buf.write("!\62\64?EP")
        return buf.getvalue()


class SecureParser ( Parser ):

    grammarFileName = "Secure.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':='", "'|'", "'->'", "'if'", 
                     "'fi'", "'do'", "'od'", "';'", "<INVALID>", "<INVALID>", 
                     "'True'", "'False'", "<INVALID>", "'*'", "'/'", "'+'", 
                     "'-'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SEP", "WHITESPACE", "NUMBER", 
                      "TRUE", "FALSE", "ID", "MUL", "DIV", "ADD", "SUB", 
                      "GT", "LT", "GE", "LE", "EQ", "NEQ", "AND", "OR", 
                      "NEG" ]

    RULE_expression = 0
    RULE_start = 1
    RULE_operatorList = 2
    RULE_operator = 3
    RULE_assignOperator = 4
    RULE_commandList = 5
    RULE_command = 6
    RULE_ifOperator = 7
    RULE_doOperator = 8

    ruleNames =  [ "expression", "start", "operatorList", "operator", "assignOperator", 
                   "commandList", "command", "ifOperator", "doOperator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    SEP=10
    WHITESPACE=11
    NUMBER=12
    TRUE=13
    FALSE=14
    ID=15
    MUL=16
    DIV=17
    ADD=18
    SUB=19
    GT=20
    LT=21
    GE=22
    LE=23
    EQ=24
    NEQ=25
    AND=26
    OR=27
    NEG=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SecureParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IdentifierContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SecureParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SecureParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SecureParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(SecureParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class BracketsContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SecureParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackets" ):
                listener.enterBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackets" ):
                listener.exitBrackets(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrackets" ):
                return visitor.visitBrackets(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(SecureParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SecureParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SecureParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(SecureParser.MUL, 0)
        def DIV(self):
            return self.getToken(SecureParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SecureParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SecureParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(SecureParser.ADD, 0)
        def SUB(self):
            return self.getToken(SecureParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SecureParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SecureParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(SecureParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class UnarySubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(SecureParser.SUB, 0)
        def expression(self):
            return self.getTypedRuleContext(SecureParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnarySub" ):
                listener.enterUnarySub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnarySub" ):
                listener.exitUnarySub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnarySub" ):
                return visitor.visitUnarySub(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(SecureParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue" ):
                listener.enterTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue" ):
                listener.exitTrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class NegateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEG(self):
            return self.getToken(SecureParser.NEG, 0)
        def expression(self):
            return self.getTypedRuleContext(SecureParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegate" ):
                listener.enterNegate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegate" ):
                listener.exitNegate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegate" ):
                return visitor.visitNegate(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(SecureParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse" ):
                listener.enterFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse" ):
                listener.exitFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class LogicContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SecureParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SecureParser.ExpressionContext,i)

        def GT(self):
            return self.getToken(SecureParser.GT, 0)
        def LT(self):
            return self.getToken(SecureParser.LT, 0)
        def GE(self):
            return self.getToken(SecureParser.GE, 0)
        def LE(self):
            return self.getToken(SecureParser.LE, 0)
        def EQ(self):
            return self.getToken(SecureParser.EQ, 0)
        def NEQ(self):
            return self.getToken(SecureParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic" ):
                listener.enterLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic" ):
                listener.exitLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic" ):
                return visitor.visitLogic(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SecureParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SecureParser.SUB]:
                localctx = SecureParser.UnarySubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 19
                self.match(SecureParser.SUB)
                self.state = 20
                self.expression(12)
                pass
            elif token in [SecureParser.NEG]:
                localctx = SecureParser.NegateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(SecureParser.NEG)
                self.state = 22
                self.expression(11)
                pass
            elif token in [SecureParser.T__0]:
                localctx = SecureParser.BracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(SecureParser.T__0)
                self.state = 24
                self.expression(0)
                self.state = 25
                self.match(SecureParser.T__1)
                pass
            elif token in [SecureParser.NUMBER]:
                localctx = SecureParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(SecureParser.NUMBER)
                pass
            elif token in [SecureParser.ID]:
                localctx = SecureParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(SecureParser.ID)
                pass
            elif token in [SecureParser.TRUE]:
                localctx = SecureParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(SecureParser.TRUE)
                pass
            elif token in [SecureParser.FALSE]:
                localctx = SecureParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(SecureParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SecureParser.MulDivContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 33
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 34
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SecureParser.MUL or _la==SecureParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = SecureParser.AddSubContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 36
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 37
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SecureParser.ADD or _la==SecureParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = SecureParser.LogicContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 39
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 40
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SecureParser.GT) | (1 << SecureParser.LT) | (1 << SecureParser.GE) | (1 << SecureParser.LE) | (1 << SecureParser.EQ) | (1 << SecureParser.NEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 41
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = SecureParser.AndContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 42
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 43
                        self.match(SecureParser.AND)
                        self.state = 44
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = SecureParser.OrContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 45
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 46
                        self.match(SecureParser.OR)
                        self.state = 47
                        self.expression(6)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operatorList(self):
            return self.getTypedRuleContext(SecureParser.OperatorListContext,0)


        def EOF(self):
            return self.getToken(SecureParser.EOF, 0)

        def getRuleIndex(self):
            return SecureParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = SecureParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.operatorList()
            self.state = 54
            self.match(SecureParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SecureParser.OperatorContext)
            else:
                return self.getTypedRuleContext(SecureParser.OperatorContext,i)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(SecureParser.SEP)
            else:
                return self.getToken(SecureParser.SEP, i)

        def getRuleIndex(self):
            return SecureParser.RULE_operatorList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorList" ):
                listener.enterOperatorList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorList" ):
                listener.exitOperatorList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorList" ):
                return visitor.visitOperatorList(self)
            else:
                return visitor.visitChildren(self)




    def operatorList(self):

        localctx = SecureParser.OperatorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operatorList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.operator()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SecureParser.SEP:
                self.state = 57
                self.match(SecureParser.SEP)
                self.state = 58
                self.operator()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignOperator(self):
            return self.getTypedRuleContext(SecureParser.AssignOperatorContext,0)


        def ifOperator(self):
            return self.getTypedRuleContext(SecureParser.IfOperatorContext,0)


        def doOperator(self):
            return self.getTypedRuleContext(SecureParser.DoOperatorContext,0)


        def getRuleIndex(self):
            return SecureParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = SecureParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operator)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SecureParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.assignOperator()
                pass
            elif token in [SecureParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.ifOperator()
                pass
            elif token in [SecureParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.doOperator()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SecureParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(SecureParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SecureParser.RULE_assignOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignOperator" ):
                listener.enterAssignOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignOperator" ):
                listener.exitAssignOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignOperator" ):
                return visitor.visitAssignOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignOperator(self):

        localctx = SecureParser.AssignOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(SecureParser.ID)
            self.state = 70
            self.match(SecureParser.T__2)
            self.state = 71
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SecureParser.CommandContext)
            else:
                return self.getTypedRuleContext(SecureParser.CommandContext,i)


        def getRuleIndex(self):
            return SecureParser.RULE_commandList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandList" ):
                listener.enterCommandList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandList" ):
                listener.exitCommandList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandList" ):
                return visitor.visitCommandList(self)
            else:
                return visitor.visitChildren(self)




    def commandList(self):

        localctx = SecureParser.CommandListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_commandList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.command()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SecureParser.T__3:
                self.state = 74
                self.match(SecureParser.T__3)
                self.state = 75
                self.command()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SecureParser.ExpressionContext,0)


        def operatorList(self):
            return self.getTypedRuleContext(SecureParser.OperatorListContext,0)


        def getRuleIndex(self):
            return SecureParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = SecureParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.expression(0)
            self.state = 82
            self.match(SecureParser.T__4)
            self.state = 83
            self.operatorList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commandList(self):
            return self.getTypedRuleContext(SecureParser.CommandListContext,0)


        def getRuleIndex(self):
            return SecureParser.RULE_ifOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfOperator" ):
                listener.enterIfOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfOperator" ):
                listener.exitIfOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfOperator" ):
                return visitor.visitIfOperator(self)
            else:
                return visitor.visitChildren(self)




    def ifOperator(self):

        localctx = SecureParser.IfOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(SecureParser.T__5)
            self.state = 86
            self.commandList()
            self.state = 87
            self.match(SecureParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commandList(self):
            return self.getTypedRuleContext(SecureParser.CommandListContext,0)


        def getRuleIndex(self):
            return SecureParser.RULE_doOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoOperator" ):
                listener.enterDoOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoOperator" ):
                listener.exitDoOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoOperator" ):
                return visitor.visitDoOperator(self)
            else:
                return visitor.visitChildren(self)




    def doOperator(self):

        localctx = SecureParser.DoOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_doOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(SecureParser.T__7)
            self.state = 90
            self.commandList()
            self.state = 91
            self.match(SecureParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         




