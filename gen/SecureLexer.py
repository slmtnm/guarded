# Generated from Secure.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("n\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\n\6\nE\n\n\r\n\16\nF\3\n\3\n\3\13\6\13L\n")
        buf.write("\13\r\13\16\13M\3\f\3\f\7\fR\n\f\f\f\16\fU\13\f\3\r\3")
        buf.write("\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\2\2\27\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27\3\2\6\5\2\13\f\17\17\"\"\3\2\62;\5\2C\\aac|\4\2C")
        buf.write("\\c|\2p\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3")
        buf.write("-\3\2\2\2\5\60\3\2\2\2\7\62\3\2\2\2\t\65\3\2\2\2\138\3")
        buf.write("\2\2\2\r;\3\2\2\2\17>\3\2\2\2\21A\3\2\2\2\23D\3\2\2\2")
        buf.write("\25K\3\2\2\2\27O\3\2\2\2\31V\3\2\2\2\33X\3\2\2\2\35Z\3")
        buf.write("\2\2\2\37\\\3\2\2\2!^\3\2\2\2#`\3\2\2\2%b\3\2\2\2\'e\3")
        buf.write("\2\2\2)h\3\2\2\2+k\3\2\2\2-.\7<\2\2./\7?\2\2/\4\3\2\2")
        buf.write("\2\60\61\7~\2\2\61\6\3\2\2\2\62\63\7/\2\2\63\64\7@\2\2")
        buf.write("\64\b\3\2\2\2\65\66\7k\2\2\66\67\7h\2\2\67\n\3\2\2\28")
        buf.write("9\7h\2\29:\7k\2\2:\f\3\2\2\2;<\7f\2\2<=\7q\2\2=\16\3\2")
        buf.write("\2\2>?\7q\2\2?@\7f\2\2@\20\3\2\2\2AB\7=\2\2B\22\3\2\2")
        buf.write("\2CE\t\2\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G")
        buf.write("H\3\2\2\2HI\b\n\2\2I\24\3\2\2\2JL\t\3\2\2KJ\3\2\2\2LM")
        buf.write("\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\26\3\2\2\2OS\t\4\2\2PR\t")
        buf.write("\5\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\30\3\2")
        buf.write("\2\2US\3\2\2\2VW\7,\2\2W\32\3\2\2\2XY\7\61\2\2Y\34\3\2")
        buf.write("\2\2Z[\7-\2\2[\36\3\2\2\2\\]\7/\2\2] \3\2\2\2^_\7@\2\2")
        buf.write("_\"\3\2\2\2`a\7>\2\2a$\3\2\2\2bc\7@\2\2cd\7?\2\2d&\3\2")
        buf.write("\2\2ef\7>\2\2fg\7?\2\2g(\3\2\2\2hi\7?\2\2ij\7?\2\2j*\3")
        buf.write("\2\2\2kl\7#\2\2lm\7?\2\2m,\3\2\2\2\6\2FMS\3\b\2\2")
        return buf.getvalue()


class SecureLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    SEP = 8
    WHITESPACE = 9
    NUMBER = 10
    ID = 11
    MUL = 12
    DIV = 13
    ADD = 14
    SUB = 15
    GT = 16
    LT = 17
    GE = 18
    LE = 19
    EQ = 20
    NEQ = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'|'", "'->'", "'if'", "'fi'", "'do'", "'od'", "';'", 
            "'*'", "'/'", "'+'", "'-'", "'>'", "'<'", "'>='", "'<='", "'=='", 
            "'!='" ]

    symbolicNames = [ "<INVALID>",
            "SEP", "WHITESPACE", "NUMBER", "ID", "MUL", "DIV", "ADD", "SUB", 
            "GT", "LT", "GE", "LE", "EQ", "NEQ" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "SEP", "WHITESPACE", "NUMBER", "ID", "MUL", "DIV", "ADD", 
                  "SUB", "GT", "LT", "GE", "LE", "EQ", "NEQ" ]

    grammarFileName = "Secure.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


