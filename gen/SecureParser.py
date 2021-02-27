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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\5\2\36\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2")
        buf.write(")\n\2\f\2\16\2,\13\2\3\3\3\3\3\3\3\4\3\4\3\4\7\4\64\n")
        buf.write("\4\f\4\16\4\67\13\4\3\5\3\5\3\5\5\5<\n\5\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\7\7E\n\7\f\7\16\7H\13\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\2\3\2\13\2\4\6\b")
        buf.write("\n\f\16\20\22\2\5\3\2\20\21\3\2\22\23\3\2\24\31\2V\2\35")
        buf.write("\3\2\2\2\4-\3\2\2\2\6\60\3\2\2\2\b;\3\2\2\2\n=\3\2\2\2")
        buf.write("\fA\3\2\2\2\16I\3\2\2\2\20M\3\2\2\2\22Q\3\2\2\2\24\25")
        buf.write("\b\2\1\2\25\26\7\23\2\2\26\36\5\2\2\t\27\30\7\3\2\2\30")
        buf.write("\31\5\2\2\2\31\32\7\4\2\2\32\36\3\2\2\2\33\36\7\16\2\2")
        buf.write("\34\36\7\17\2\2\35\24\3\2\2\2\35\27\3\2\2\2\35\33\3\2")
        buf.write("\2\2\35\34\3\2\2\2\36*\3\2\2\2\37 \f\7\2\2 !\t\2\2\2!")
        buf.write(")\5\2\2\b\"#\f\6\2\2#$\t\3\2\2$)\5\2\2\7%&\f\5\2\2&\'")
        buf.write("\t\4\2\2\')\5\2\2\6(\37\3\2\2\2(\"\3\2\2\2(%\3\2\2\2)")
        buf.write(",\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\3\3\2\2\2,*\3\2\2\2-.\5")
        buf.write("\6\4\2./\7\2\2\3/\5\3\2\2\2\60\65\5\b\5\2\61\62\7\f\2")
        buf.write("\2\62\64\5\b\5\2\63\61\3\2\2\2\64\67\3\2\2\2\65\63\3\2")
        buf.write("\2\2\65\66\3\2\2\2\66\7\3\2\2\2\67\65\3\2\2\28<\5\n\6")
        buf.write("\29<\5\20\t\2:<\5\22\n\2;8\3\2\2\2;9\3\2\2\2;:\3\2\2\2")
        buf.write("<\t\3\2\2\2=>\7\17\2\2>?\7\5\2\2?@\5\2\2\2@\13\3\2\2\2")
        buf.write("AF\5\16\b\2BC\7\6\2\2CE\5\16\b\2DB\3\2\2\2EH\3\2\2\2F")
        buf.write("D\3\2\2\2FG\3\2\2\2G\r\3\2\2\2HF\3\2\2\2IJ\5\2\2\2JK\7")
        buf.write("\7\2\2KL\5\6\4\2L\17\3\2\2\2MN\7\b\2\2NO\5\f\7\2OP\7\t")
        buf.write("\2\2P\21\3\2\2\2QR\7\n\2\2RS\5\f\7\2ST\7\13\2\2T\23\3")
        buf.write("\2\2\2\b\35(*\65;F")
        return buf.getvalue()


class SecureParser ( Parser ):

    grammarFileName = "Secure.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':='", "'|'", "'->'", "'if'", 
                     "'fi'", "'do'", "'od'", "';'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'>'", "'<'", 
                     "'>='", "'<='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SEP", "WHITESPACE", "NUMBER", 
                      "ID", "MUL", "DIV", "ADD", "SUB", "GT", "LT", "GE", 
                      "LE", "EQ", "NEQ" ]

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
    ID=13
    MUL=14
    DIV=15
    ADD=16
    SUB=17
    GT=18
    LT=19
    GE=20
    LE=21
    EQ=22
    NEQ=23

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
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SecureParser.SUB]:
                localctx = SecureParser.UnarySubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 19
                self.match(SecureParser.SUB)
                self.state = 20
                self.expression(7)
                pass
            elif token in [SecureParser.T__0]:
                localctx = SecureParser.BracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(SecureParser.T__0)
                self.state = 22
                self.expression(0)
                self.state = 23
                self.match(SecureParser.T__1)
                pass
            elif token in [SecureParser.NUMBER]:
                localctx = SecureParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(SecureParser.NUMBER)
                pass
            elif token in [SecureParser.ID]:
                localctx = SecureParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(SecureParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SecureParser.MulDivContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 29
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 30
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SecureParser.MUL or _la==SecureParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = SecureParser.AddSubContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 32
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 33
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SecureParser.ADD or _la==SecureParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = SecureParser.LogicContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 35
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 36
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SecureParser.GT) | (1 << SecureParser.LT) | (1 << SecureParser.GE) | (1 << SecureParser.LE) | (1 << SecureParser.EQ) | (1 << SecureParser.NEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        self.expression(4)
                        pass

             
                self.state = 42
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
            self.state = 43
            self.operatorList()
            self.state = 44
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
            self.state = 46
            self.operator()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SecureParser.SEP:
                self.state = 47
                self.match(SecureParser.SEP)
                self.state = 48
                self.operator()
                self.state = 53
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
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SecureParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.assignOperator()
                pass
            elif token in [SecureParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.ifOperator()
                pass
            elif token in [SecureParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
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
            self.state = 59
            self.match(SecureParser.ID)
            self.state = 60
            self.match(SecureParser.T__2)
            self.state = 61
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
            self.state = 63
            self.command()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SecureParser.T__3:
                self.state = 64
                self.match(SecureParser.T__3)
                self.state = 65
                self.command()
                self.state = 70
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
            self.state = 71
            self.expression(0)
            self.state = 72
            self.match(SecureParser.T__4)
            self.state = 73
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
            self.state = 75
            self.match(SecureParser.T__5)
            self.state = 76
            self.commandList()
            self.state = 77
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
            self.state = 79
            self.match(SecureParser.T__7)
            self.state = 80
            self.commandList()
            self.state = 81
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




