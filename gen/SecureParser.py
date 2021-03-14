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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"")
        buf.write("m\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2$\n\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\7\2;\n\2\f\2\16\2>\13\2\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\7\4G\n\4\f\4\16\4J\13\4\3\5\3\5\3\5\5\5O")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7\7X\n\7\f\7\16\7[\13")
        buf.write("\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\2\3\2\f\2\4\6\b\n\f\16\20\22\24\2")
        buf.write("\5\3\2\24\25\3\2\26\27\3\2\30\35\2s\2#\3\2\2\2\4?\3\2")
        buf.write("\2\2\6C\3\2\2\2\bN\3\2\2\2\nP\3\2\2\2\fT\3\2\2\2\16\\")
        buf.write("\3\2\2\2\20`\3\2\2\2\22d\3\2\2\2\24h\3\2\2\2\26\27\b\2")
        buf.write("\1\2\27\30\7\27\2\2\30$\5\2\2\20\31\32\7 \2\2\32$\5\2")
        buf.write("\2\17\33\34\7\3\2\2\34\35\5\2\2\2\35\36\7\4\2\2\36$\3")
        buf.write("\2\2\2\37$\7\20\2\2 $\7\23\2\2!$\7\21\2\2\"$\7\22\2\2")
        buf.write("#\26\3\2\2\2#\31\3\2\2\2#\33\3\2\2\2#\37\3\2\2\2# \3\2")
        buf.write("\2\2#!\3\2\2\2#\"\3\2\2\2$<\3\2\2\2%&\f\r\2\2&\'\t\2\2")
        buf.write("\2\';\5\2\2\16()\f\f\2\2)*\t\3\2\2*;\5\2\2\r+,\f\13\2")
        buf.write("\2,-\t\4\2\2-;\5\2\2\f./\f\n\2\2/\60\7\36\2\2\60;\5\2")
        buf.write("\2\13\61\62\f\t\2\2\62\63\7\37\2\2\63;\5\2\2\n\64\65\f")
        buf.write("\b\2\2\65\66\7!\2\2\66;\5\2\2\t\678\f\7\2\289\7\"\2\2")
        buf.write("9;\5\2\2\b:%\3\2\2\2:(\3\2\2\2:+\3\2\2\2:.\3\2\2\2:\61")
        buf.write("\3\2\2\2:\64\3\2\2\2:\67\3\2\2\2;>\3\2\2\2<:\3\2\2\2<")
        buf.write("=\3\2\2\2=\3\3\2\2\2><\3\2\2\2?@\5\6\4\2@A\5\24\13\2A")
        buf.write("B\7\2\2\3B\5\3\2\2\2CH\5\b\5\2DE\7\16\2\2EG\5\b\5\2FD")
        buf.write("\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\7\3\2\2\2JH\3")
        buf.write("\2\2\2KO\5\n\6\2LO\5\20\t\2MO\5\22\n\2NK\3\2\2\2NL\3\2")
        buf.write("\2\2NM\3\2\2\2O\t\3\2\2\2PQ\7\23\2\2QR\7\5\2\2RS\5\2\2")
        buf.write("\2S\13\3\2\2\2TY\5\16\b\2UV\7\6\2\2VX\5\16\b\2WU\3\2\2")
        buf.write("\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\r\3\2\2\2[Y\3\2\2\2")
        buf.write("\\]\5\2\2\2]^\7\7\2\2^_\5\6\4\2_\17\3\2\2\2`a\7\b\2\2")
        buf.write("ab\5\f\7\2bc\7\t\2\2c\21\3\2\2\2de\7\n\2\2ef\5\f\7\2f")
        buf.write("g\7\13\2\2g\23\3\2\2\2hi\7\f\2\2ij\5\2\2\2jk\7\r\2\2k")
        buf.write("\25\3\2\2\2\b#:<HNY")
        return buf.getvalue()


class SecureParser ( Parser ):

    grammarFileName = "Secure.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':='", "'|'", "'->'", "'if'", 
                     "'fi'", "'do'", "'od'", "'['", "']'", "';'", "<INVALID>", 
                     "<INVALID>", "'True'", "'False'", "<INVALID>", "'*'", 
                     "'/'", "'+'", "'-'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'&&'", "'||'", "'!'", "'=>'", "'<=>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SEP", "WHITESPACE", "NUMBER", "TRUE", "FALSE", "ID", 
                      "MUL", "DIV", "ADD", "SUB", "GT", "LT", "GE", "LE", 
                      "EQ", "NEQ", "AND", "OR", "NEG", "IMPL", "EQUIV" ]

    RULE_expression = 0
    RULE_start = 1
    RULE_operatorList = 2
    RULE_operator = 3
    RULE_assignOperator = 4
    RULE_commandList = 5
    RULE_command = 6
    RULE_ifOperator = 7
    RULE_doOperator = 8
    RULE_postCondition = 9

    ruleNames =  [ "expression", "start", "operatorList", "operator", "assignOperator", 
                   "commandList", "command", "ifOperator", "doOperator", 
                   "postCondition" ]

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
    T__9=10
    T__10=11
    SEP=12
    WHITESPACE=13
    NUMBER=14
    TRUE=15
    FALSE=16
    ID=17
    MUL=18
    DIV=19
    ADD=20
    SUB=21
    GT=22
    LT=23
    GE=24
    LE=25
    EQ=26
    NEQ=27
    AND=28
    OR=29
    NEG=30
    IMPL=31
    EQUIV=32

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


    class ImplContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SecureParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SecureParser.ExpressionContext,i)

        def IMPL(self):
            return self.getToken(SecureParser.IMPL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpl" ):
                listener.enterImpl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpl" ):
                listener.exitImpl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpl" ):
                return visitor.visitImpl(self)
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


    class EquivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SecureParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SecureParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SecureParser.ExpressionContext,i)

        def EQUIV(self):
            return self.getToken(SecureParser.EQUIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquiv" ):
                listener.enterEquiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquiv" ):
                listener.exitEquiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquiv" ):
                return visitor.visitEquiv(self)
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
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SecureParser.SUB]:
                localctx = SecureParser.UnarySubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 21
                self.match(SecureParser.SUB)
                self.state = 22
                self.expression(14)
                pass
            elif token in [SecureParser.NEG]:
                localctx = SecureParser.NegateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(SecureParser.NEG)
                self.state = 24
                self.expression(13)
                pass
            elif token in [SecureParser.T__0]:
                localctx = SecureParser.BracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(SecureParser.T__0)
                self.state = 26
                self.expression(0)
                self.state = 27
                self.match(SecureParser.T__1)
                pass
            elif token in [SecureParser.NUMBER]:
                localctx = SecureParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(SecureParser.NUMBER)
                pass
            elif token in [SecureParser.ID]:
                localctx = SecureParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(SecureParser.ID)
                pass
            elif token in [SecureParser.TRUE]:
                localctx = SecureParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(SecureParser.TRUE)
                pass
            elif token in [SecureParser.FALSE]:
                localctx = SecureParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(SecureParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 56
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SecureParser.MulDivContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 35
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 36
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SecureParser.MUL or _la==SecureParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = SecureParser.AddSubContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 38
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 39
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SecureParser.ADD or _la==SecureParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        self.expression(11)
                        pass

                    elif la_ == 3:
                        localctx = SecureParser.LogicContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 41
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 42
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SecureParser.GT) | (1 << SecureParser.LT) | (1 << SecureParser.GE) | (1 << SecureParser.LE) | (1 << SecureParser.EQ) | (1 << SecureParser.NEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        self.expression(10)
                        pass

                    elif la_ == 4:
                        localctx = SecureParser.AndContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 44
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 45
                        self.match(SecureParser.AND)
                        self.state = 46
                        self.expression(9)
                        pass

                    elif la_ == 5:
                        localctx = SecureParser.OrContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 47
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 48
                        self.match(SecureParser.OR)
                        self.state = 49
                        self.expression(8)
                        pass

                    elif la_ == 6:
                        localctx = SecureParser.ImplContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 50
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 51
                        self.match(SecureParser.IMPL)
                        self.state = 52
                        self.expression(7)
                        pass

                    elif la_ == 7:
                        localctx = SecureParser.EquivContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 53
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 54
                        self.match(SecureParser.EQUIV)
                        self.state = 55
                        self.expression(6)
                        pass

             
                self.state = 60
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


        def postCondition(self):
            return self.getTypedRuleContext(SecureParser.PostConditionContext,0)


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
            self.state = 61
            self.operatorList()
            self.state = 62
            self.postCondition()
            self.state = 63
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
            self.state = 65
            self.operator()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SecureParser.SEP:
                self.state = 66
                self.match(SecureParser.SEP)
                self.state = 67
                self.operator()
                self.state = 72
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
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SecureParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.assignOperator()
                pass
            elif token in [SecureParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.ifOperator()
                pass
            elif token in [SecureParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
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
            self.state = 78
            self.match(SecureParser.ID)
            self.state = 79
            self.match(SecureParser.T__2)
            self.state = 80
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
            self.state = 82
            self.command()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SecureParser.T__3:
                self.state = 83
                self.match(SecureParser.T__3)
                self.state = 84
                self.command()
                self.state = 89
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
            self.state = 90
            self.expression(0)
            self.state = 91
            self.match(SecureParser.T__4)
            self.state = 92
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
            self.state = 94
            self.match(SecureParser.T__5)
            self.state = 95
            self.commandList()
            self.state = 96
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
            self.state = 98
            self.match(SecureParser.T__7)
            self.state = 99
            self.commandList()
            self.state = 100
            self.match(SecureParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SecureParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SecureParser.RULE_postCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostCondition" ):
                listener.enterPostCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostCondition" ):
                listener.exitPostCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostCondition" ):
                return visitor.visitPostCondition(self)
            else:
                return visitor.visitChildren(self)




    def postCondition(self):

        localctx = SecureParser.PostConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_postCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(SecureParser.T__9)
            self.state = 103
            self.expression(0)
            self.state = 104
            self.match(SecureParser.T__10)
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
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         




