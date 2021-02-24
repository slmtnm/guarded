// Code generated from Secure.g4 by ANTLR 4.9.1. DO NOT EDIT.

package parser

import (
	"fmt"
	"unicode"

	"github.com/antlr/antlr4/runtime/Go/antlr"
)

// Suppress unused import error
var _ = fmt.Printf
var _ = unicode.IsLetter

var serializedLexerAtn = []uint16{
	3, 24715, 42794, 33075, 47597, 16764, 15335, 30598, 22884, 2, 21, 102,
	8, 1, 4, 2, 9, 2, 4, 3, 9, 3, 4, 4, 9, 4, 4, 5, 9, 5, 4, 6, 9, 6, 4, 7,
	9, 7, 4, 8, 9, 8, 4, 9, 9, 9, 4, 10, 9, 10, 4, 11, 9, 11, 4, 12, 9, 12,
	4, 13, 9, 13, 4, 14, 9, 14, 4, 15, 9, 15, 4, 16, 9, 16, 4, 17, 9, 17, 4,
	18, 9, 18, 4, 19, 9, 19, 4, 20, 9, 20, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3,
	4, 3, 4, 3, 4, 3, 5, 3, 5, 3, 5, 3, 6, 3, 6, 3, 6, 3, 7, 3, 7, 3, 8, 6,
	8, 59, 10, 8, 13, 8, 14, 8, 60, 3, 8, 3, 8, 3, 9, 3, 9, 7, 9, 67, 10, 9,
	12, 9, 14, 9, 70, 11, 9, 3, 10, 3, 10, 7, 10, 74, 10, 10, 12, 10, 14, 10,
	77, 11, 10, 3, 11, 3, 11, 3, 12, 3, 12, 3, 13, 3, 13, 3, 14, 3, 14, 3,
	15, 3, 15, 3, 16, 3, 16, 3, 17, 3, 17, 3, 17, 3, 18, 3, 18, 3, 18, 3, 19,
	3, 19, 3, 19, 3, 20, 3, 20, 3, 20, 2, 2, 21, 3, 3, 5, 4, 7, 5, 9, 6, 11,
	7, 13, 8, 15, 9, 17, 10, 19, 11, 21, 12, 23, 13, 25, 14, 27, 15, 29, 16,
	31, 17, 33, 18, 35, 19, 37, 20, 39, 21, 3, 2, 7, 5, 2, 11, 12, 15, 15,
	34, 34, 3, 2, 51, 59, 3, 2, 50, 59, 5, 2, 67, 92, 97, 97, 99, 124, 4, 2,
	67, 92, 99, 124, 2, 104, 2, 3, 3, 2, 2, 2, 2, 5, 3, 2, 2, 2, 2, 7, 3, 2,
	2, 2, 2, 9, 3, 2, 2, 2, 2, 11, 3, 2, 2, 2, 2, 13, 3, 2, 2, 2, 2, 15, 3,
	2, 2, 2, 2, 17, 3, 2, 2, 2, 2, 19, 3, 2, 2, 2, 2, 21, 3, 2, 2, 2, 2, 23,
	3, 2, 2, 2, 2, 25, 3, 2, 2, 2, 2, 27, 3, 2, 2, 2, 2, 29, 3, 2, 2, 2, 2,
	31, 3, 2, 2, 2, 2, 33, 3, 2, 2, 2, 2, 35, 3, 2, 2, 2, 2, 37, 3, 2, 2, 2,
	2, 39, 3, 2, 2, 2, 3, 41, 3, 2, 2, 2, 5, 44, 3, 2, 2, 2, 7, 46, 3, 2, 2,
	2, 9, 49, 3, 2, 2, 2, 11, 52, 3, 2, 2, 2, 13, 55, 3, 2, 2, 2, 15, 58, 3,
	2, 2, 2, 17, 64, 3, 2, 2, 2, 19, 71, 3, 2, 2, 2, 21, 78, 3, 2, 2, 2, 23,
	80, 3, 2, 2, 2, 25, 82, 3, 2, 2, 2, 27, 84, 3, 2, 2, 2, 29, 86, 3, 2, 2,
	2, 31, 88, 3, 2, 2, 2, 33, 90, 3, 2, 2, 2, 35, 93, 3, 2, 2, 2, 37, 96,
	3, 2, 2, 2, 39, 99, 3, 2, 2, 2, 41, 42, 7, 60, 2, 2, 42, 43, 7, 63, 2,
	2, 43, 4, 3, 2, 2, 2, 44, 45, 7, 126, 2, 2, 45, 6, 3, 2, 2, 2, 46, 47,
	7, 47, 2, 2, 47, 48, 7, 64, 2, 2, 48, 8, 3, 2, 2, 2, 49, 50, 7, 107, 2,
	2, 50, 51, 7, 104, 2, 2, 51, 10, 3, 2, 2, 2, 52, 53, 7, 104, 2, 2, 53,
	54, 7, 107, 2, 2, 54, 12, 3, 2, 2, 2, 55, 56, 7, 61, 2, 2, 56, 14, 3, 2,
	2, 2, 57, 59, 9, 2, 2, 2, 58, 57, 3, 2, 2, 2, 59, 60, 3, 2, 2, 2, 60, 58,
	3, 2, 2, 2, 60, 61, 3, 2, 2, 2, 61, 62, 3, 2, 2, 2, 62, 63, 8, 8, 2, 2,
	63, 16, 3, 2, 2, 2, 64, 68, 9, 3, 2, 2, 65, 67, 9, 4, 2, 2, 66, 65, 3,
	2, 2, 2, 67, 70, 3, 2, 2, 2, 68, 66, 3, 2, 2, 2, 68, 69, 3, 2, 2, 2, 69,
	18, 3, 2, 2, 2, 70, 68, 3, 2, 2, 2, 71, 75, 9, 5, 2, 2, 72, 74, 9, 6, 2,
	2, 73, 72, 3, 2, 2, 2, 74, 77, 3, 2, 2, 2, 75, 73, 3, 2, 2, 2, 75, 76,
	3, 2, 2, 2, 76, 20, 3, 2, 2, 2, 77, 75, 3, 2, 2, 2, 78, 79, 7, 44, 2, 2,
	79, 22, 3, 2, 2, 2, 80, 81, 7, 49, 2, 2, 81, 24, 3, 2, 2, 2, 82, 83, 7,
	45, 2, 2, 83, 26, 3, 2, 2, 2, 84, 85, 7, 47, 2, 2, 85, 28, 3, 2, 2, 2,
	86, 87, 7, 64, 2, 2, 87, 30, 3, 2, 2, 2, 88, 89, 7, 62, 2, 2, 89, 32, 3,
	2, 2, 2, 90, 91, 7, 64, 2, 2, 91, 92, 7, 63, 2, 2, 92, 34, 3, 2, 2, 2,
	93, 94, 7, 62, 2, 2, 94, 95, 7, 63, 2, 2, 95, 36, 3, 2, 2, 2, 96, 97, 7,
	63, 2, 2, 97, 98, 7, 63, 2, 2, 98, 38, 3, 2, 2, 2, 99, 100, 7, 35, 2, 2,
	100, 101, 7, 63, 2, 2, 101, 40, 3, 2, 2, 2, 6, 2, 60, 68, 75, 3, 8, 2,
	2,
}

var lexerChannelNames = []string{
	"DEFAULT_TOKEN_CHANNEL", "HIDDEN",
}

var lexerModeNames = []string{
	"DEFAULT_MODE",
}

var lexerLiteralNames = []string{
	"", "':='", "'|'", "'->'", "'if'", "'fi'", "';'", "", "", "", "'*'", "'/'",
	"'+'", "'-'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='",
}

var lexerSymbolicNames = []string{
	"", "", "", "", "", "", "SEP", "WHITESPACE", "NUMBER", "ID", "MUL", "DIV",
	"ADD", "SUB", "GT", "LT", "GE", "LE", "EQ", "NEQ",
}

var lexerRuleNames = []string{
	"T__0", "T__1", "T__2", "T__3", "T__4", "SEP", "WHITESPACE", "NUMBER",
	"ID", "MUL", "DIV", "ADD", "SUB", "GT", "LT", "GE", "LE", "EQ", "NEQ",
}

type SecureLexer struct {
	*antlr.BaseLexer
	channelNames []string
	modeNames    []string
	// TODO: EOF string
}

// NewSecureLexer produces a new lexer instance for the optional input antlr.CharStream.
//
// The *SecureLexer instance produced may be reused by calling the SetInputStream method.
// The initial lexer configuration is expensive to construct, and the object is not thread-safe;
// however, if used within a Golang sync.Pool, the construction cost amortizes well and the
// objects can be used in a thread-safe manner.
func NewSecureLexer(input antlr.CharStream) *SecureLexer {
	l := new(SecureLexer)
	lexerDeserializer := antlr.NewATNDeserializer(nil)
	lexerAtn := lexerDeserializer.DeserializeFromUInt16(serializedLexerAtn)
	lexerDecisionToDFA := make([]*antlr.DFA, len(lexerAtn.DecisionToState))
	for index, ds := range lexerAtn.DecisionToState {
		lexerDecisionToDFA[index] = antlr.NewDFA(ds, index)
	}
	l.BaseLexer = antlr.NewBaseLexer(input)
	l.Interpreter = antlr.NewLexerATNSimulator(l, lexerAtn, lexerDecisionToDFA, antlr.NewPredictionContextCache())

	l.channelNames = lexerChannelNames
	l.modeNames = lexerModeNames
	l.RuleNames = lexerRuleNames
	l.LiteralNames = lexerLiteralNames
	l.SymbolicNames = lexerSymbolicNames
	l.GrammarFileName = "Secure.g4"
	// TODO: l.EOF = antlr.TokenEOF

	return l
}

// SecureLexer tokens.
const (
	SecureLexerT__0       = 1
	SecureLexerT__1       = 2
	SecureLexerT__2       = 3
	SecureLexerT__3       = 4
	SecureLexerT__4       = 5
	SecureLexerSEP        = 6
	SecureLexerWHITESPACE = 7
	SecureLexerNUMBER     = 8
	SecureLexerID         = 9
	SecureLexerMUL        = 10
	SecureLexerDIV        = 11
	SecureLexerADD        = 12
	SecureLexerSUB        = 13
	SecureLexerGT         = 14
	SecureLexerLT         = 15
	SecureLexerGE         = 16
	SecureLexerLE         = 17
	SecureLexerEQ         = 18
	SecureLexerNEQ        = 19
)
