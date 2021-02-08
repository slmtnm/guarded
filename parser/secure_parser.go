// Code generated from Secure.g4 by ANTLR 4.9.1. DO NOT EDIT.

package parser // Secure

import (
	"fmt"
	"reflect"
	"strconv"

	"github.com/antlr/antlr4/runtime/Go/antlr"
)

// Suppress unused import errors
var _ = fmt.Printf
var _ = reflect.Copy
var _ = strconv.Itoa

var parserATN = []uint16{
	3, 24715, 42794, 33075, 47597, 16764, 15335, 30598, 22884, 3, 21, 68, 4,
	2, 9, 2, 4, 3, 9, 3, 4, 4, 9, 4, 4, 5, 9, 5, 4, 6, 9, 6, 4, 7, 9, 7, 4,
	8, 9, 8, 3, 2, 3, 2, 3, 2, 7, 2, 20, 10, 2, 12, 2, 14, 2, 23, 11, 2, 3,
	2, 3, 2, 3, 3, 3, 3, 5, 3, 29, 10, 3, 3, 4, 3, 4, 3, 4, 3, 4, 3, 5, 3,
	5, 3, 5, 3, 5, 3, 6, 3, 6, 3, 6, 7, 6, 42, 10, 6, 12, 6, 14, 6, 45, 11,
	6, 3, 7, 3, 7, 3, 7, 3, 7, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3,
	8, 3, 8, 3, 8, 3, 8, 3, 8, 7, 8, 63, 10, 8, 12, 8, 14, 8, 66, 11, 8, 3,
	8, 2, 3, 14, 9, 2, 4, 6, 8, 10, 12, 14, 2, 5, 3, 2, 12, 13, 3, 2, 14, 15,
	3, 2, 16, 21, 2, 66, 2, 16, 3, 2, 2, 2, 4, 28, 3, 2, 2, 2, 6, 30, 3, 2,
	2, 2, 8, 34, 3, 2, 2, 2, 10, 38, 3, 2, 2, 2, 12, 46, 3, 2, 2, 2, 14, 50,
	3, 2, 2, 2, 16, 21, 5, 4, 3, 2, 17, 18, 7, 8, 2, 2, 18, 20, 5, 4, 3, 2,
	19, 17, 3, 2, 2, 2, 20, 23, 3, 2, 2, 2, 21, 19, 3, 2, 2, 2, 21, 22, 3,
	2, 2, 2, 22, 24, 3, 2, 2, 2, 23, 21, 3, 2, 2, 2, 24, 25, 7, 2, 2, 3, 25,
	3, 3, 2, 2, 2, 26, 29, 5, 6, 4, 2, 27, 29, 5, 8, 5, 2, 28, 26, 3, 2, 2,
	2, 28, 27, 3, 2, 2, 2, 29, 5, 3, 2, 2, 2, 30, 31, 7, 11, 2, 2, 31, 32,
	7, 3, 2, 2, 32, 33, 5, 14, 8, 2, 33, 7, 3, 2, 2, 2, 34, 35, 7, 4, 2, 2,
	35, 36, 5, 10, 6, 2, 36, 37, 7, 5, 2, 2, 37, 9, 3, 2, 2, 2, 38, 43, 5,
	12, 7, 2, 39, 40, 7, 6, 2, 2, 40, 42, 5, 12, 7, 2, 41, 39, 3, 2, 2, 2,
	42, 45, 3, 2, 2, 2, 43, 41, 3, 2, 2, 2, 43, 44, 3, 2, 2, 2, 44, 11, 3,
	2, 2, 2, 45, 43, 3, 2, 2, 2, 46, 47, 5, 14, 8, 2, 47, 48, 7, 7, 2, 2, 48,
	49, 5, 4, 3, 2, 49, 13, 3, 2, 2, 2, 50, 51, 8, 8, 1, 2, 51, 52, 7, 10,
	2, 2, 52, 64, 3, 2, 2, 2, 53, 54, 12, 6, 2, 2, 54, 55, 9, 2, 2, 2, 55,
	63, 5, 14, 8, 7, 56, 57, 12, 5, 2, 2, 57, 58, 9, 3, 2, 2, 58, 63, 5, 14,
	8, 6, 59, 60, 12, 4, 2, 2, 60, 61, 9, 4, 2, 2, 61, 63, 5, 14, 8, 5, 62,
	53, 3, 2, 2, 2, 62, 56, 3, 2, 2, 2, 62, 59, 3, 2, 2, 2, 63, 66, 3, 2, 2,
	2, 64, 62, 3, 2, 2, 2, 64, 65, 3, 2, 2, 2, 65, 15, 3, 2, 2, 2, 66, 64,
	3, 2, 2, 2, 7, 21, 28, 43, 62, 64,
}
var literalNames = []string{
	"", "':='", "'if'", "'fi'", "'|'", "'->'", "';'", "", "", "", "'*'", "'/'",
	"'+'", "'-'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='",
}
var symbolicNames = []string{
	"", "", "", "", "", "", "SEP", "WHITESPACE", "NUMBER", "ID", "MUL", "DIV",
	"ADD", "SUB", "GT", "LT", "GE", "LE", "EQ", "NEQ",
}

var ruleNames = []string{
	"start", "operator", "assignOperator", "ifOperator", "commandList", "command",
	"expression",
}

type SecureParser struct {
	*antlr.BaseParser
}

// NewSecureParser produces a new parser instance for the optional input antlr.TokenStream.
//
// The *SecureParser instance produced may be reused by calling the SetInputStream method.
// The initial parser configuration is expensive to construct, and the object is not thread-safe;
// however, if used within a Golang sync.Pool, the construction cost amortizes well and the
// objects can be used in a thread-safe manner.
func NewSecureParser(input antlr.TokenStream) *SecureParser {
	this := new(SecureParser)
	deserializer := antlr.NewATNDeserializer(nil)
	deserializedATN := deserializer.DeserializeFromUInt16(parserATN)
	decisionToDFA := make([]*antlr.DFA, len(deserializedATN.DecisionToState))
	for index, ds := range deserializedATN.DecisionToState {
		decisionToDFA[index] = antlr.NewDFA(ds, index)
	}
	this.BaseParser = antlr.NewBaseParser(input)

	this.Interpreter = antlr.NewParserATNSimulator(this, deserializedATN, decisionToDFA, antlr.NewPredictionContextCache())
	this.RuleNames = ruleNames
	this.LiteralNames = literalNames
	this.SymbolicNames = symbolicNames
	this.GrammarFileName = "Secure.g4"

	return this
}

// SecureParser tokens.
const (
	SecureParserEOF        = antlr.TokenEOF
	SecureParserT__0       = 1
	SecureParserT__1       = 2
	SecureParserT__2       = 3
	SecureParserT__3       = 4
	SecureParserT__4       = 5
	SecureParserSEP        = 6
	SecureParserWHITESPACE = 7
	SecureParserNUMBER     = 8
	SecureParserID         = 9
	SecureParserMUL        = 10
	SecureParserDIV        = 11
	SecureParserADD        = 12
	SecureParserSUB        = 13
	SecureParserGT         = 14
	SecureParserLT         = 15
	SecureParserGE         = 16
	SecureParserLE         = 17
	SecureParserEQ         = 18
	SecureParserNEQ        = 19
)

// SecureParser rules.
const (
	SecureParserRULE_start          = 0
	SecureParserRULE_operator       = 1
	SecureParserRULE_assignOperator = 2
	SecureParserRULE_ifOperator     = 3
	SecureParserRULE_commandList    = 4
	SecureParserRULE_command        = 5
	SecureParserRULE_expression     = 6
)

// IStartContext is an interface to support dynamic dispatch.
type IStartContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsStartContext differentiates from other interfaces.
	IsStartContext()
}

type StartContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyStartContext() *StartContext {
	var p = new(StartContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = SecureParserRULE_start
	return p
}

func (*StartContext) IsStartContext() {}

func NewStartContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *StartContext {
	var p = new(StartContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = SecureParserRULE_start

	return p
}

func (s *StartContext) GetParser() antlr.Parser { return s.parser }

func (s *StartContext) AllOperator() []IOperatorContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*IOperatorContext)(nil)).Elem())
	var tst = make([]IOperatorContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(IOperatorContext)
		}
	}

	return tst
}

func (s *StartContext) Operator(i int) IOperatorContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IOperatorContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(IOperatorContext)
}

func (s *StartContext) EOF() antlr.TerminalNode {
	return s.GetToken(SecureParserEOF, 0)
}

func (s *StartContext) AllSEP() []antlr.TerminalNode {
	return s.GetTokens(SecureParserSEP)
}

func (s *StartContext) SEP(i int) antlr.TerminalNode {
	return s.GetToken(SecureParserSEP, i)
}

func (s *StartContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *StartContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *StartContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterStart(s)
	}
}

func (s *StartContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitStart(s)
	}
}

func (p *SecureParser) Start() (localctx IStartContext) {
	localctx = NewStartContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 0, SecureParserRULE_start)
	var _la int

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(14)
		p.Operator()
	}
	p.SetState(19)
	p.GetErrorHandler().Sync(p)
	_la = p.GetTokenStream().LA(1)

	for _la == SecureParserSEP {
		{
			p.SetState(15)
			p.Match(SecureParserSEP)
		}
		{
			p.SetState(16)
			p.Operator()
		}

		p.SetState(21)
		p.GetErrorHandler().Sync(p)
		_la = p.GetTokenStream().LA(1)
	}
	{
		p.SetState(22)
		p.Match(SecureParserEOF)
	}

	return localctx
}

// IOperatorContext is an interface to support dynamic dispatch.
type IOperatorContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsOperatorContext differentiates from other interfaces.
	IsOperatorContext()
}

type OperatorContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyOperatorContext() *OperatorContext {
	var p = new(OperatorContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = SecureParserRULE_operator
	return p
}

func (*OperatorContext) IsOperatorContext() {}

func NewOperatorContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *OperatorContext {
	var p = new(OperatorContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = SecureParserRULE_operator

	return p
}

func (s *OperatorContext) GetParser() antlr.Parser { return s.parser }

func (s *OperatorContext) AssignOperator() IAssignOperatorContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IAssignOperatorContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IAssignOperatorContext)
}

func (s *OperatorContext) IfOperator() IIfOperatorContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IIfOperatorContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IIfOperatorContext)
}

func (s *OperatorContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *OperatorContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *OperatorContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterOperator(s)
	}
}

func (s *OperatorContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitOperator(s)
	}
}

func (p *SecureParser) Operator() (localctx IOperatorContext) {
	localctx = NewOperatorContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 2, SecureParserRULE_operator)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.SetState(26)
	p.GetErrorHandler().Sync(p)

	switch p.GetTokenStream().LA(1) {
	case SecureParserID:
		p.EnterOuterAlt(localctx, 1)
		{
			p.SetState(24)
			p.AssignOperator()
		}

	case SecureParserT__1:
		p.EnterOuterAlt(localctx, 2)
		{
			p.SetState(25)
			p.IfOperator()
		}

	default:
		panic(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
	}

	return localctx
}

// IAssignOperatorContext is an interface to support dynamic dispatch.
type IAssignOperatorContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsAssignOperatorContext differentiates from other interfaces.
	IsAssignOperatorContext()
}

type AssignOperatorContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyAssignOperatorContext() *AssignOperatorContext {
	var p = new(AssignOperatorContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = SecureParserRULE_assignOperator
	return p
}

func (*AssignOperatorContext) IsAssignOperatorContext() {}

func NewAssignOperatorContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *AssignOperatorContext {
	var p = new(AssignOperatorContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = SecureParserRULE_assignOperator

	return p
}

func (s *AssignOperatorContext) GetParser() antlr.Parser { return s.parser }

func (s *AssignOperatorContext) ID() antlr.TerminalNode {
	return s.GetToken(SecureParserID, 0)
}

func (s *AssignOperatorContext) Expression() IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *AssignOperatorContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *AssignOperatorContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *AssignOperatorContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterAssignOperator(s)
	}
}

func (s *AssignOperatorContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitAssignOperator(s)
	}
}

func (p *SecureParser) AssignOperator() (localctx IAssignOperatorContext) {
	localctx = NewAssignOperatorContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 4, SecureParserRULE_assignOperator)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(28)
		p.Match(SecureParserID)
	}
	{
		p.SetState(29)
		p.Match(SecureParserT__0)
	}
	{
		p.SetState(30)
		p.expression(0)
	}

	return localctx
}

// IIfOperatorContext is an interface to support dynamic dispatch.
type IIfOperatorContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsIfOperatorContext differentiates from other interfaces.
	IsIfOperatorContext()
}

type IfOperatorContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyIfOperatorContext() *IfOperatorContext {
	var p = new(IfOperatorContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = SecureParserRULE_ifOperator
	return p
}

func (*IfOperatorContext) IsIfOperatorContext() {}

func NewIfOperatorContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *IfOperatorContext {
	var p = new(IfOperatorContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = SecureParserRULE_ifOperator

	return p
}

func (s *IfOperatorContext) GetParser() antlr.Parser { return s.parser }

func (s *IfOperatorContext) CommandList() ICommandListContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*ICommandListContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(ICommandListContext)
}

func (s *IfOperatorContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *IfOperatorContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *IfOperatorContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterIfOperator(s)
	}
}

func (s *IfOperatorContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitIfOperator(s)
	}
}

func (p *SecureParser) IfOperator() (localctx IIfOperatorContext) {
	localctx = NewIfOperatorContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 6, SecureParserRULE_ifOperator)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(32)
		p.Match(SecureParserT__1)
	}
	{
		p.SetState(33)
		p.CommandList()
	}
	{
		p.SetState(34)
		p.Match(SecureParserT__2)
	}

	return localctx
}

// ICommandListContext is an interface to support dynamic dispatch.
type ICommandListContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsCommandListContext differentiates from other interfaces.
	IsCommandListContext()
}

type CommandListContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyCommandListContext() *CommandListContext {
	var p = new(CommandListContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = SecureParserRULE_commandList
	return p
}

func (*CommandListContext) IsCommandListContext() {}

func NewCommandListContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *CommandListContext {
	var p = new(CommandListContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = SecureParserRULE_commandList

	return p
}

func (s *CommandListContext) GetParser() antlr.Parser { return s.parser }

func (s *CommandListContext) AllCommand() []ICommandContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*ICommandContext)(nil)).Elem())
	var tst = make([]ICommandContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(ICommandContext)
		}
	}

	return tst
}

func (s *CommandListContext) Command(i int) ICommandContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*ICommandContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(ICommandContext)
}

func (s *CommandListContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *CommandListContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *CommandListContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterCommandList(s)
	}
}

func (s *CommandListContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitCommandList(s)
	}
}

func (p *SecureParser) CommandList() (localctx ICommandListContext) {
	localctx = NewCommandListContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 8, SecureParserRULE_commandList)
	var _la int

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(36)
		p.Command()
	}
	p.SetState(41)
	p.GetErrorHandler().Sync(p)
	_la = p.GetTokenStream().LA(1)

	for _la == SecureParserT__3 {
		{
			p.SetState(37)
			p.Match(SecureParserT__3)
		}
		{
			p.SetState(38)
			p.Command()
		}

		p.SetState(43)
		p.GetErrorHandler().Sync(p)
		_la = p.GetTokenStream().LA(1)
	}

	return localctx
}

// ICommandContext is an interface to support dynamic dispatch.
type ICommandContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsCommandContext differentiates from other interfaces.
	IsCommandContext()
}

type CommandContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyCommandContext() *CommandContext {
	var p = new(CommandContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = SecureParserRULE_command
	return p
}

func (*CommandContext) IsCommandContext() {}

func NewCommandContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *CommandContext {
	var p = new(CommandContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = SecureParserRULE_command

	return p
}

func (s *CommandContext) GetParser() antlr.Parser { return s.parser }

func (s *CommandContext) Expression() IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *CommandContext) Operator() IOperatorContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IOperatorContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IOperatorContext)
}

func (s *CommandContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *CommandContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *CommandContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterCommand(s)
	}
}

func (s *CommandContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitCommand(s)
	}
}

func (p *SecureParser) Command() (localctx ICommandContext) {
	localctx = NewCommandContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 10, SecureParserRULE_command)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(44)
		p.expression(0)
	}
	{
		p.SetState(45)
		p.Match(SecureParserT__4)
	}
	{
		p.SetState(46)
		p.Operator()
	}

	return localctx
}

// IExpressionContext is an interface to support dynamic dispatch.
type IExpressionContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsExpressionContext differentiates from other interfaces.
	IsExpressionContext()
}

type ExpressionContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyExpressionContext() *ExpressionContext {
	var p = new(ExpressionContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = SecureParserRULE_expression
	return p
}

func (*ExpressionContext) IsExpressionContext() {}

func NewExpressionContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *ExpressionContext {
	var p = new(ExpressionContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = SecureParserRULE_expression

	return p
}

func (s *ExpressionContext) GetParser() antlr.Parser { return s.parser }

func (s *ExpressionContext) CopyFrom(ctx *ExpressionContext) {
	s.BaseParserRuleContext.CopyFrom(ctx.BaseParserRuleContext)
}

func (s *ExpressionContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ExpressionContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

type NumberContext struct {
	*ExpressionContext
}

func NewNumberContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *NumberContext {
	var p = new(NumberContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *NumberContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *NumberContext) NUMBER() antlr.TerminalNode {
	return s.GetToken(SecureParserNUMBER, 0)
}

func (s *NumberContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterNumber(s)
	}
}

func (s *NumberContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitNumber(s)
	}
}

type MulDivContext struct {
	*ExpressionContext
	op antlr.Token
}

func NewMulDivContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *MulDivContext {
	var p = new(MulDivContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *MulDivContext) GetOp() antlr.Token { return s.op }

func (s *MulDivContext) SetOp(v antlr.Token) { s.op = v }

func (s *MulDivContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *MulDivContext) AllExpression() []IExpressionContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*IExpressionContext)(nil)).Elem())
	var tst = make([]IExpressionContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(IExpressionContext)
		}
	}

	return tst
}

func (s *MulDivContext) Expression(i int) IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *MulDivContext) MUL() antlr.TerminalNode {
	return s.GetToken(SecureParserMUL, 0)
}

func (s *MulDivContext) DIV() antlr.TerminalNode {
	return s.GetToken(SecureParserDIV, 0)
}

func (s *MulDivContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterMulDiv(s)
	}
}

func (s *MulDivContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitMulDiv(s)
	}
}

type AddSubContext struct {
	*ExpressionContext
	op antlr.Token
}

func NewAddSubContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *AddSubContext {
	var p = new(AddSubContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *AddSubContext) GetOp() antlr.Token { return s.op }

func (s *AddSubContext) SetOp(v antlr.Token) { s.op = v }

func (s *AddSubContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *AddSubContext) AllExpression() []IExpressionContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*IExpressionContext)(nil)).Elem())
	var tst = make([]IExpressionContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(IExpressionContext)
		}
	}

	return tst
}

func (s *AddSubContext) Expression(i int) IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *AddSubContext) ADD() antlr.TerminalNode {
	return s.GetToken(SecureParserADD, 0)
}

func (s *AddSubContext) SUB() antlr.TerminalNode {
	return s.GetToken(SecureParserSUB, 0)
}

func (s *AddSubContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterAddSub(s)
	}
}

func (s *AddSubContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitAddSub(s)
	}
}

type LogicContext struct {
	*ExpressionContext
	op antlr.Token
}

func NewLogicContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *LogicContext {
	var p = new(LogicContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *LogicContext) GetOp() antlr.Token { return s.op }

func (s *LogicContext) SetOp(v antlr.Token) { s.op = v }

func (s *LogicContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *LogicContext) AllExpression() []IExpressionContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*IExpressionContext)(nil)).Elem())
	var tst = make([]IExpressionContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(IExpressionContext)
		}
	}

	return tst
}

func (s *LogicContext) Expression(i int) IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *LogicContext) GT() antlr.TerminalNode {
	return s.GetToken(SecureParserGT, 0)
}

func (s *LogicContext) LT() antlr.TerminalNode {
	return s.GetToken(SecureParserLT, 0)
}

func (s *LogicContext) GE() antlr.TerminalNode {
	return s.GetToken(SecureParserGE, 0)
}

func (s *LogicContext) LE() antlr.TerminalNode {
	return s.GetToken(SecureParserLE, 0)
}

func (s *LogicContext) EQ() antlr.TerminalNode {
	return s.GetToken(SecureParserEQ, 0)
}

func (s *LogicContext) NEQ() antlr.TerminalNode {
	return s.GetToken(SecureParserNEQ, 0)
}

func (s *LogicContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterLogic(s)
	}
}

func (s *LogicContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitLogic(s)
	}
}

func (p *SecureParser) Expression() (localctx IExpressionContext) {
	return p.expression(0)
}

func (p *SecureParser) expression(_p int) (localctx IExpressionContext) {
	var _parentctx antlr.ParserRuleContext = p.GetParserRuleContext()
	_parentState := p.GetState()
	localctx = NewExpressionContext(p, p.GetParserRuleContext(), _parentState)
	var _prevctx IExpressionContext = localctx
	var _ antlr.ParserRuleContext = _prevctx // TODO: To prevent unused variable warning.
	_startState := 12
	p.EnterRecursionRule(localctx, 12, SecureParserRULE_expression, _p)
	var _la int

	defer func() {
		p.UnrollRecursionContexts(_parentctx)
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	var _alt int

	p.EnterOuterAlt(localctx, 1)
	localctx = NewNumberContext(p, localctx)
	p.SetParserRuleContext(localctx)
	_prevctx = localctx

	{
		p.SetState(49)
		p.Match(SecureParserNUMBER)
	}

	p.GetParserRuleContext().SetStop(p.GetTokenStream().LT(-1))
	p.SetState(62)
	p.GetErrorHandler().Sync(p)
	_alt = p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 4, p.GetParserRuleContext())

	for _alt != 2 && _alt != antlr.ATNInvalidAltNumber {
		if _alt == 1 {
			if p.GetParseListeners() != nil {
				p.TriggerExitRuleEvent()
			}
			_prevctx = localctx
			p.SetState(60)
			p.GetErrorHandler().Sync(p)
			switch p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 3, p.GetParserRuleContext()) {
			case 1:
				localctx = NewMulDivContext(p, NewExpressionContext(p, _parentctx, _parentState))
				p.PushNewRecursionContext(localctx, _startState, SecureParserRULE_expression)
				p.SetState(51)

				if !(p.Precpred(p.GetParserRuleContext(), 4)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 4)", ""))
				}
				{
					p.SetState(52)

					var _lt = p.GetTokenStream().LT(1)

					localctx.(*MulDivContext).op = _lt

					_la = p.GetTokenStream().LA(1)

					if !(_la == SecureParserMUL || _la == SecureParserDIV) {
						var _ri = p.GetErrorHandler().RecoverInline(p)

						localctx.(*MulDivContext).op = _ri
					} else {
						p.GetErrorHandler().ReportMatch(p)
						p.Consume()
					}
				}
				{
					p.SetState(53)
					p.expression(5)
				}

			case 2:
				localctx = NewAddSubContext(p, NewExpressionContext(p, _parentctx, _parentState))
				p.PushNewRecursionContext(localctx, _startState, SecureParserRULE_expression)
				p.SetState(54)

				if !(p.Precpred(p.GetParserRuleContext(), 3)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 3)", ""))
				}
				{
					p.SetState(55)

					var _lt = p.GetTokenStream().LT(1)

					localctx.(*AddSubContext).op = _lt

					_la = p.GetTokenStream().LA(1)

					if !(_la == SecureParserADD || _la == SecureParserSUB) {
						var _ri = p.GetErrorHandler().RecoverInline(p)

						localctx.(*AddSubContext).op = _ri
					} else {
						p.GetErrorHandler().ReportMatch(p)
						p.Consume()
					}
				}
				{
					p.SetState(56)
					p.expression(4)
				}

			case 3:
				localctx = NewLogicContext(p, NewExpressionContext(p, _parentctx, _parentState))
				p.PushNewRecursionContext(localctx, _startState, SecureParserRULE_expression)
				p.SetState(57)

				if !(p.Precpred(p.GetParserRuleContext(), 2)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 2)", ""))
				}
				{
					p.SetState(58)

					var _lt = p.GetTokenStream().LT(1)

					localctx.(*LogicContext).op = _lt

					_la = p.GetTokenStream().LA(1)

					if !(((_la)&-(0x1f+1)) == 0 && ((1<<uint(_la))&((1<<SecureParserGT)|(1<<SecureParserLT)|(1<<SecureParserGE)|(1<<SecureParserLE)|(1<<SecureParserEQ)|(1<<SecureParserNEQ))) != 0) {
						var _ri = p.GetErrorHandler().RecoverInline(p)

						localctx.(*LogicContext).op = _ri
					} else {
						p.GetErrorHandler().ReportMatch(p)
						p.Consume()
					}
				}
				{
					p.SetState(59)
					p.expression(3)
				}

			}

		}
		p.SetState(64)
		p.GetErrorHandler().Sync(p)
		_alt = p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 4, p.GetParserRuleContext())
	}

	return localctx
}

func (p *SecureParser) Sempred(localctx antlr.RuleContext, ruleIndex, predIndex int) bool {
	switch ruleIndex {
	case 6:
		var t *ExpressionContext = nil
		if localctx != nil {
			t = localctx.(*ExpressionContext)
		}
		return p.Expression_Sempred(t, predIndex)

	default:
		panic("No predicate with index: " + fmt.Sprint(ruleIndex))
	}
}

func (p *SecureParser) Expression_Sempred(localctx antlr.RuleContext, predIndex int) bool {
	switch predIndex {
	case 0:
		return p.Precpred(p.GetParserRuleContext(), 4)

	case 1:
		return p.Precpred(p.GetParserRuleContext(), 3)

	case 2:
		return p.Precpred(p.GetParserRuleContext(), 2)

	default:
		panic("No predicate with index: " + fmt.Sprint(predIndex))
	}
}
