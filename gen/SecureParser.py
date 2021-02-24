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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("O\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\5\2\30\n\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2#\n\2\f\2\16\2&\13\2\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\7\4.\n\4\f\4\16\4\61\13\4\3\5\3\5")
        buf.write("\5\5\65\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7\7>\n\7\f\7\16")
        buf.write("\7A\13\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\2\3\2\13\2\4\6\b\n\f\16\20\22\2\5\3\2\16\17\3\2")
        buf.write("\20\21\3\2\22\27\2L\2\27\3\2\2\2\4\'\3\2\2\2\6*\3\2\2")
        buf.write("\2\b\64\3\2\2\2\n\66\3\2\2\2\f:\3\2\2\2\16B\3\2\2\2\20")
        buf.write("F\3\2\2\2\22J\3\2\2\2\24\25\b\2\1\2\25\30\7\f\2\2\26\30")
        buf.write("\7\r\2\2\27\24\3\2\2\2\27\26\3\2\2\2\30$\3\2\2\2\31\32")
        buf.write("\f\7\2\2\32\33\t\2\2\2\33#\5\2\2\b\34\35\f\6\2\2\35\36")
        buf.write("\t\3\2\2\36#\5\2\2\7\37 \f\5\2\2 !\t\4\2\2!#\5\2\2\6\"")
        buf.write("\31\3\2\2\2\"\34\3\2\2\2\"\37\3\2\2\2#&\3\2\2\2$\"\3\2")
        buf.write("\2\2$%\3\2\2\2%\3\3\2\2\2&$\3\2\2\2\'(\5\6\4\2()\7\2\2")
        buf.write("\3)\5\3\2\2\2*/\5\b\5\2+,\7\n\2\2,.\5\b\5\2-+\3\2\2\2")
        buf.write(".\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\7\3\2\2\2\61/\3")
        buf.write("\2\2\2\62\65\5\n\6\2\63\65\5\20\t\2\64\62\3\2\2\2\64\63")
        buf.write("\3\2\2\2\65\t\3\2\2\2\66\67\7\r\2\2\678\7\3\2\289\5\2")
        buf.write("\2\29\13\3\2\2\2:?\5\16\b\2;<\7\4\2\2<>\5\16\b\2=;\3\2")
        buf.write("\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\r\3\2\2\2A?\3\2\2")
        buf.write("\2BC\5\2\2\2CD\7\5\2\2DE\5\b\5\2E\17\3\2\2\2FG\7\6\2\2")
        buf.write("GH\5\f\7\2HI\7\7\2\2I\21\3\2\2\2JK\7\b\2\2KL\5\f\7\2L")
        buf.write("M\7\t\2\2M\23\3\2\2\2\b\27\"$/\64?")
        return buf.getvalue()


class SecureParser ( Parser ):

    grammarFileName = "Secure.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'|'", "'->'", "'if'", "'fi'", 
                     "'do'", "'od'", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'*'", "'/'", "'+'", "'-'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SEP", "WHITESPACE", "NUMBER", "ID", "MUL", "DIV", 
                      "ADD", "SUB", "GT", "LT", "GE", "LE", "EQ", "NEQ" ]

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
    SEP=8
    WHITESPACE=9
    NUMBER=10
    ID=11
    MUL=12
    DIV=13
    ADD=14
    SUB=15
    GT=16
    LT=17
    GE=18
    LE=19
    EQ=20
    NEQ=21

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
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SecureParser.NUMBER]:
                localctx = SecureParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 19
                self.match(SecureParser.NUMBER)
                pass
            elif token in [SecureParser.ID]:
                localctx = SecureParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(SecureParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 32
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SecureParser.MulDivContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 23
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 24
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SecureParser.MUL or _la==SecureParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = SecureParser.AddSubContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 26
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 27
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SecureParser.ADD or _la==SecureParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = SecureParser.LogicContext(self, SecureParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 29
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 30
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SecureParser.GT) | (1 << SecureParser.LT) | (1 << SecureParser.GE) | (1 << SecureParser.LE) | (1 << SecureParser.EQ) | (1 << SecureParser.NEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.expression(4)
                        pass

             
                self.state = 36
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
            self.state = 37
            self.operatorList()
            self.state = 38
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
            self.state = 40
            self.operator()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SecureParser.SEP:
                self.state = 41
                self.match(SecureParser.SEP)
                self.state = 42
                self.operator()
                self.state = 47
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
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SecureParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.assignOperator()
                pass
            elif token in [SecureParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.ifOperator()
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
            self.state = 52
            self.match(SecureParser.ID)
            self.state = 53
            self.match(SecureParser.T__0)
            self.state = 54
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
            self.state = 56
            self.command()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SecureParser.T__1:
                self.state = 57
                self.match(SecureParser.T__1)
                self.state = 58
                self.command()
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


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SecureParser.ExpressionContext,0)


        def operator(self):
            return self.getTypedRuleContext(SecureParser.OperatorContext,0)


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
            self.state = 64
            self.expression(0)
            self.state = 65
            self.match(SecureParser.T__2)
            self.state = 66
            self.operator()
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
            self.state = 68
            self.match(SecureParser.T__3)
            self.state = 69
            self.commandList()
            self.state = 70
            self.match(SecureParser.T__4)
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
            self.state = 72
            self.match(SecureParser.T__5)
            self.state = 73
            self.commandList()
            self.state = 74
            self.match(SecureParser.T__6)
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
         




