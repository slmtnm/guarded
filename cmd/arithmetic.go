package cmd

import (
	"fmt"
	"strconv"

	"github.com/slmtnm/secure/parser"
)

func (l *secureListener) ExitMulDiv(c *parser.MulDivContext) {
	right, left := l.stack.pop().(float64), l.stack.pop().(float64)

	switch c.GetOp().GetTokenType() {
	case parser.SecureParserMUL:
		l.stack.push(left * right)
	case parser.SecureParserDIV:
		l.stack.push(left / right)
	default:
		panic(fmt.Sprintf("unexpected op: %s", c.GetOp().GetText()))
	}
}

func (l *secureListener) ExitAddSub(c *parser.AddSubContext) {
	right, left := l.stack.pop().(float64), l.stack.pop().(float64)

	switch c.GetOp().GetTokenType() {
	case parser.SecureParserADD:
		l.stack.push(left + right)
	case parser.SecureParserSUB:
		l.stack.push(left - right)
	default:
		panic(fmt.Sprintf("unexpected op: %s", c.GetOp().GetText()))
	}
}

func (l *secureListener) ExitNumber(c *parser.NumberContext) {
	i, err := strconv.ParseFloat(c.GetText(), 64)
	if err != nil {
		panic(err.Error())
	}

	l.stack.push(i)
}

func (l *secureListener) ExitIdentifier(c *parser.IdentifierContext) {
	varName := c.GetText()
	value, ok := l.vars[varName]

	if !ok {
		panic(fmt.Errorf("Undeclared identifier %v", varName))
	}

	l.stack.push(value.(float64))
}

func (l *secureListener) ExitLogic(c *parser.LogicContext) {
	right, left := l.stack.pop().(float64), l.stack.pop().(float64)

	switch c.GetOp().GetTokenType() {
	case parser.SecureParserLT:
		if left < right {
			l.stack.push(true)
		} else {
			l.stack.push(false)
		}
	case parser.SecureParserLE:
		if left <= right {
			l.stack.push(true)
		} else {
			l.stack.push(false)
		}
	case parser.SecureParserGT:
		if left > right {
			l.stack.push(true)
		} else {
			l.stack.push(false)
		}
	case parser.SecureParserGE:
		if left >= right {
			l.stack.push(true)
		} else {
			l.stack.push(false)
		}
	case parser.SecureParserEQ:
		if left == right {
			l.stack.push(true)
		} else {
			l.stack.push(false)
		}
	case parser.SecureParserNEQ:
		if left != right {
			l.stack.push(true)
		} else {
			l.stack.push(false)
		}
	default:
		panic(fmt.Sprintf("unexpected op: %s", c.GetOp().GetText()))
	}
}
