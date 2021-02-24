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
	3, 24715, 42794, 33075, 47597, 16764, 15335, 30598, 22884, 3, 21, 73, 4,
	2, 9, 2, 4, 3, 9, 3, 4, 4, 9, 4, 4, 5, 9, 5, 4, 6, 9, 6, 4, 7, 9, 7, 4,
	8, 9, 8, 4, 9, 9, 9, 3, 2, 3, 2, 3, 2, 5, 2, 22, 10, 2, 3, 2, 3, 2, 3,
	2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 7, 2, 33, 10, 2, 12, 2, 14, 2, 36,
	11, 2, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 3, 4, 7, 4, 44, 10, 4, 12, 4, 14,
	4, 47, 11, 4, 3, 5, 3, 5, 5, 5, 51, 10, 5, 3, 6, 3, 6, 3, 6, 3, 6, 3, 7,
	3, 7, 3, 7, 7, 7, 60, 10, 7, 12, 7, 14, 7, 63, 11, 7, 3, 8, 3, 8, 3, 8,
	3, 8, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 2, 3, 2, 10, 2, 4, 6, 8, 10, 12, 14,
	16, 2, 5, 3, 2, 12, 13, 3, 2, 14, 15, 3, 2, 16, 21, 2, 71, 2, 21, 3, 2,
	2, 2, 4, 37, 3, 2, 2, 2, 6, 40, 3, 2, 2, 2, 8, 50, 3, 2, 2, 2, 10, 52,
	3, 2, 2, 2, 12, 56, 3, 2, 2, 2, 14, 64, 3, 2, 2, 2, 16, 68, 3, 2, 2, 2,
	18, 19, 8, 2, 1, 2, 19, 22, 7, 10, 2, 2, 20, 22, 7, 11, 2, 2, 21, 18, 3,
	2, 2, 2, 21, 20, 3, 2, 2, 2, 22, 34, 3, 2, 2, 2, 23, 24, 12, 7, 2, 2, 24,
	25, 9, 2, 2, 2, 25, 33, 5, 2, 2, 8, 26, 27, 12, 6, 2, 2, 27, 28, 9, 3,
	2, 2, 28, 33, 5, 2, 2, 7, 29, 30, 12, 5, 2, 2, 30, 31, 9, 4, 2, 2, 31,
	33, 5, 2, 2, 6, 32, 23, 3, 2, 2, 2, 32, 26, 3, 2, 2, 2, 32, 29, 3, 2, 2,
	2, 33, 36, 3, 2, 2, 2, 34, 32, 3, 2, 2, 2, 34, 35, 3, 2, 2, 2, 35, 3, 3,
	2, 2, 2, 36, 34, 3, 2, 2, 2, 37, 38, 5, 6, 4, 2, 38, 39, 7, 2, 2, 3, 39,
	5, 3, 2, 2, 2, 40, 45, 5, 8, 5, 2, 41, 42, 7, 8, 2, 2, 42, 44, 5, 8, 5,
	2, 43, 41, 3, 2, 2, 2, 44, 47, 3, 2, 2, 2, 45, 43, 3, 2, 2, 2, 45, 46,
	3, 2, 2, 2, 46, 7, 3, 2, 2, 2, 47, 45, 3, 2, 2, 2, 48, 51, 5, 10, 6, 2,
	49, 51, 5, 16, 9, 2, 50, 48, 3, 2, 2, 2, 50, 49, 3, 2, 2, 2, 51, 9, 3,
	2, 2, 2, 52, 53, 7, 11, 2, 2, 53, 54, 7, 3, 2, 2, 54, 55, 5, 2, 2, 2, 55,
	11, 3, 2, 2, 2, 56, 61, 5, 14, 8, 2, 57, 58, 7, 4, 2, 2, 58, 60, 5, 14,
	8, 2, 59, 57, 3, 2, 2, 2, 60, 63, 3, 2, 2, 2, 61, 59, 3, 2, 2, 2, 61, 62,
	3, 2, 2, 2, 62, 13, 3, 2, 2, 2, 63, 61, 3, 2, 2, 2, 64, 65, 5, 2, 2, 2,
	65, 66, 7, 5, 2, 2, 66, 67, 5, 8, 5, 2, 67, 15, 3, 2, 2, 2, 68, 69, 7,
	6, 2, 2, 69, 70, 5, 12, 7, 2, 70, 71, 7, 7, 2, 2, 71, 17, 3, 2, 2, 2, 8,
	21, 32, 34, 45, 50, 61,
}
var literalNames = []string{
	"", "':='", "'|'", "'->'", "'if'", "'fi'", "';'", "", "", "", "'*'", "'/'",
	"'+'", "'-'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='",
}
var symbolicNames = []string{
	"", "", "", "", "", "", "SEP", "WHITESPACE", "NUMBER", "ID", "MUL", "DIV",
	"ADD", "SUB", "GT", "LT", "GE", "LE", "EQ", "NEQ",
}

var ruleNames = []string{
	"expression", "start", "operatorList", "operator", "assignOperator", "commandList",
	"command", "ifOperator",
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
	SecureParserRULE_expression     = 0
	SecureParserRULE_start          = 1
	SecureParserRULE_operatorList   = 2
	SecureParserRULE_operator       = 3
	SecureParserRULE_assignOperator = 4
	SecureParserRULE_commandList    = 5
	SecureParserRULE_command        = 6
	SecureParserRULE_ifOperator     = 7
)

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

type IdentifierContext struct {
	*ExpressionContext
}

func NewIdentifierContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *IdentifierContext {
	var p = new(IdentifierContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *IdentifierContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *IdentifierContext) ID() antlr.TerminalNode {
	return s.GetToken(SecureParserID, 0)
}

func (s *IdentifierContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterIdentifier(s)
	}
}

func (s *IdentifierContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitIdentifier(s)
	}
}

func (s *IdentifierContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitIdentifier(s)

	default:
		return t.VisitChildren(s)
	}
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

func (s *NumberContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitNumber(s)

	default:
		return t.VisitChildren(s)
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

func (s *MulDivContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitMulDiv(s)

	default:
		return t.VisitChildren(s)
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

func (s *AddSubContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitAddSub(s)

	default:
		return t.VisitChildren(s)
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

func (s *LogicContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitLogic(s)

	default:
		return t.VisitChildren(s)
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
	_startState := 0
	p.EnterRecursionRule(localctx, 0, SecureParserRULE_expression, _p)
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
	p.SetState(19)
	p.GetErrorHandler().Sync(p)

	switch p.GetTokenStream().LA(1) {
	case SecureParserNUMBER:
		localctx = NewNumberContext(p, localctx)
		p.SetParserRuleContext(localctx)
		_prevctx = localctx

		{
			p.SetState(17)
			p.Match(SecureParserNUMBER)
		}

	case SecureParserID:
		localctx = NewIdentifierContext(p, localctx)
		p.SetParserRuleContext(localctx)
		_prevctx = localctx
		{
			p.SetState(18)
			p.Match(SecureParserID)
		}

	default:
		panic(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
	}
	p.GetParserRuleContext().SetStop(p.GetTokenStream().LT(-1))
	p.SetState(32)
	p.GetErrorHandler().Sync(p)
	_alt = p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 2, p.GetParserRuleContext())

	for _alt != 2 && _alt != antlr.ATNInvalidAltNumber {
		if _alt == 1 {
			if p.GetParseListeners() != nil {
				p.TriggerExitRuleEvent()
			}
			_prevctx = localctx
			p.SetState(30)
			p.GetErrorHandler().Sync(p)
			switch p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 1, p.GetParserRuleContext()) {
			case 1:
				localctx = NewMulDivContext(p, NewExpressionContext(p, _parentctx, _parentState))
				p.PushNewRecursionContext(localctx, _startState, SecureParserRULE_expression)
				p.SetState(21)

				if !(p.Precpred(p.GetParserRuleContext(), 5)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 5)", ""))
				}
				{
					p.SetState(22)

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
					p.SetState(23)
					p.expression(6)
				}

			case 2:
				localctx = NewAddSubContext(p, NewExpressionContext(p, _parentctx, _parentState))
				p.PushNewRecursionContext(localctx, _startState, SecureParserRULE_expression)
				p.SetState(24)

				if !(p.Precpred(p.GetParserRuleContext(), 4)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 4)", ""))
				}
				{
					p.SetState(25)

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
					p.SetState(26)
					p.expression(5)
				}

			case 3:
				localctx = NewLogicContext(p, NewExpressionContext(p, _parentctx, _parentState))
				p.PushNewRecursionContext(localctx, _startState, SecureParserRULE_expression)
				p.SetState(27)

				if !(p.Precpred(p.GetParserRuleContext(), 3)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 3)", ""))
				}
				{
					p.SetState(28)

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
					p.SetState(29)
					p.expression(4)
				}

			}

		}
		p.SetState(34)
		p.GetErrorHandler().Sync(p)
		_alt = p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 2, p.GetParserRuleContext())
	}

	return localctx
}

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

func (s *StartContext) OperatorList() IOperatorListContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IOperatorListContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IOperatorListContext)
}

func (s *StartContext) EOF() antlr.TerminalNode {
	return s.GetToken(SecureParserEOF, 0)
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

func (s *StartContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitStart(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *SecureParser) Start() (localctx IStartContext) {
	localctx = NewStartContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 2, SecureParserRULE_start)

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
		p.SetState(35)
		p.OperatorList()
	}
	{
		p.SetState(36)
		p.Match(SecureParserEOF)
	}

	return localctx
}

// IOperatorListContext is an interface to support dynamic dispatch.
type IOperatorListContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsOperatorListContext differentiates from other interfaces.
	IsOperatorListContext()
}

type OperatorListContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyOperatorListContext() *OperatorListContext {
	var p = new(OperatorListContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = SecureParserRULE_operatorList
	return p
}

func (*OperatorListContext) IsOperatorListContext() {}

func NewOperatorListContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *OperatorListContext {
	var p = new(OperatorListContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = SecureParserRULE_operatorList

	return p
}

func (s *OperatorListContext) GetParser() antlr.Parser { return s.parser }

func (s *OperatorListContext) AllOperator() []IOperatorContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*IOperatorContext)(nil)).Elem())
	var tst = make([]IOperatorContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(IOperatorContext)
		}
	}

	return tst
}

func (s *OperatorListContext) Operator(i int) IOperatorContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IOperatorContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(IOperatorContext)
}

func (s *OperatorListContext) AllSEP() []antlr.TerminalNode {
	return s.GetTokens(SecureParserSEP)
}

func (s *OperatorListContext) SEP(i int) antlr.TerminalNode {
	return s.GetToken(SecureParserSEP, i)
}

func (s *OperatorListContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *OperatorListContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *OperatorListContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.EnterOperatorList(s)
	}
}

func (s *OperatorListContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(SecureListener); ok {
		listenerT.ExitOperatorList(s)
	}
}

func (s *OperatorListContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitOperatorList(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *SecureParser) OperatorList() (localctx IOperatorListContext) {
	localctx = NewOperatorListContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 4, SecureParserRULE_operatorList)
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
		p.SetState(38)
		p.Operator()
	}
	p.SetState(43)
	p.GetErrorHandler().Sync(p)
	_la = p.GetTokenStream().LA(1)

	for _la == SecureParserSEP {
		{
			p.SetState(39)
			p.Match(SecureParserSEP)
		}
		{
			p.SetState(40)
			p.Operator()
		}

		p.SetState(45)
		p.GetErrorHandler().Sync(p)
		_la = p.GetTokenStream().LA(1)
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

func (s *OperatorContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitOperator(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *SecureParser) Operator() (localctx IOperatorContext) {
	localctx = NewOperatorContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 6, SecureParserRULE_operator)

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

	p.SetState(48)
	p.GetErrorHandler().Sync(p)

	switch p.GetTokenStream().LA(1) {
	case SecureParserID:
		p.EnterOuterAlt(localctx, 1)
		{
			p.SetState(46)
			p.AssignOperator()
		}

	case SecureParserT__3:
		p.EnterOuterAlt(localctx, 2)
		{
			p.SetState(47)
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

func (s *AssignOperatorContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitAssignOperator(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *SecureParser) AssignOperator() (localctx IAssignOperatorContext) {
	localctx = NewAssignOperatorContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 8, SecureParserRULE_assignOperator)

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
		p.SetState(50)
		p.Match(SecureParserID)
	}
	{
		p.SetState(51)
		p.Match(SecureParserT__0)
	}
	{
		p.SetState(52)
		p.expression(0)
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

func (s *CommandListContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitCommandList(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *SecureParser) CommandList() (localctx ICommandListContext) {
	localctx = NewCommandListContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 10, SecureParserRULE_commandList)
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
		p.SetState(54)
		p.Command()
	}
	p.SetState(59)
	p.GetErrorHandler().Sync(p)
	_la = p.GetTokenStream().LA(1)

	for _la == SecureParserT__1 {
		{
			p.SetState(55)
			p.Match(SecureParserT__1)
		}
		{
			p.SetState(56)
			p.Command()
		}

		p.SetState(61)
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

func (s *CommandContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitCommand(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *SecureParser) Command() (localctx ICommandContext) {
	localctx = NewCommandContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 12, SecureParserRULE_command)

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
		p.SetState(62)
		p.expression(0)
	}
	{
		p.SetState(63)
		p.Match(SecureParserT__2)
	}
	{
		p.SetState(64)
		p.Operator()
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

func (s *IfOperatorContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case SecureVisitor:
		return t.VisitIfOperator(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *SecureParser) IfOperator() (localctx IIfOperatorContext) {
	localctx = NewIfOperatorContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 14, SecureParserRULE_ifOperator)

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
		p.SetState(66)
		p.Match(SecureParserT__3)
	}
	{
		p.SetState(67)
		p.CommandList()
	}
	{
		p.SetState(68)
		p.Match(SecureParserT__4)
	}

	return localctx
}

func (p *SecureParser) Sempred(localctx antlr.RuleContext, ruleIndex, predIndex int) bool {
	switch ruleIndex {
	case 0:
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
		return p.Precpred(p.GetParserRuleContext(), 5)

	case 1:
		return p.Precpred(p.GetParserRuleContext(), 4)

	case 2:
		return p.Precpred(p.GetParserRuleContext(), 3)

	default:
		panic("No predicate with index: " + fmt.Sprint(predIndex))
	}
}
