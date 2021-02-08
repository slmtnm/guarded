package cmd

import (
	"fmt"
	"log"
	"strconv"

	"github.com/slmtnm/secure/parser"

	"github.com/antlr/antlr4/runtime/Go/antlr"
)

// Vars is a map containing all variable that defined
// with assign operator
var Vars map[string]float64 = make(map[string]float64)

type secureListener struct {
	*parser.BaseSecureListener
	stack []float64
}

func (l *secureListener) push(i float64) {
	l.stack = append(l.stack, i)
}

func (l *secureListener) pop() float64 {
	if len(l.stack) < 1 {
		panic("stack is empty unable to pop")
	}

	// Get the last value from the stack.
	result := l.stack[len(l.stack)-1]

	// Remove the last element from the stack.
	l.stack = l.stack[:len(l.stack)-1]

	return result
}

func (l *secureListener) ExitMulDiv(c *parser.MulDivContext) {
	right, left := l.pop(), l.pop()

	switch c.GetOp().GetTokenType() {
	case parser.SecureParserMUL:
		l.push(left * right)
	case parser.SecureParserDIV:
		l.push(left / right)
	default:
		panic(fmt.Sprintf("unexpected op: %s", c.GetOp().GetText()))
	}
}

func (l *secureListener) ExitAddSub(c *parser.AddSubContext) {
	right, left := l.pop(), l.pop()

	switch c.GetOp().GetTokenType() {
	case parser.SecureParserADD:
		l.push(left + right)
	case parser.SecureParserSUB:
		l.push(left - right)
	default:
		panic(fmt.Sprintf("unexpected op: %s", c.GetOp().GetText()))
	}
}

func (l *secureListener) ExitNumber(c *parser.NumberContext) {
	i, err := strconv.ParseFloat(c.GetText(), 64)
	if err != nil {
		panic(err.Error())
	}

	l.push(i)
}

func (l *secureListener) ExitLogic(c *parser.LogicContext) {
	right, left := l.pop(), l.pop()

	switch c.GetOp().GetTokenType() {
	case parser.SecureParserLT:
		if left < right {
			l.push(1)
		} else {
			l.push(0)
		}
	case parser.SecureParserLE:
		if left <= right {
			l.push(1)
		} else {
			l.push(0)
		}
	case parser.SecureParserGT:
		if left > right {
			l.push(1)
		} else {
			l.push(0)
		}
	case parser.SecureParserGE:
		if left >= right {
			l.push(1)
		} else {
			l.push(0)
		}
	case parser.SecureParserEQ:
		if left == right {
			l.push(1)
		} else {
			l.push(0)
		}
	case parser.SecureParserNEQ:
		if left != right {
			l.push(1)
		} else {
			l.push(0)
		}
	default:
		panic(fmt.Sprintf("unexpected op: %s", c.GetOp().GetText()))
	}
}

func (l *secureListener) ExitAssignOperator(c *parser.AssignOperatorContext) {
	operands := c.GetChildren()

	if len(operands) != 3 {
		log.Fatal("Assign operator must have exactly 3 child nodes")
	}

	name, ok := operands[0].GetPayload().(*antlr.CommonToken)
	if !ok {
		log.Fatal("Could not cast first operand")
	}

	varName := name.GetText()
	varValue := l.pop()

	Vars[varName] = varValue
}

func (l *secureListener) ExitIfOperator(c *parser.IfOperatorContext) {
	children := c.GetChildren()

	if len(children) != 3 {
		log.Fatal("If operator must have exactly 3 child nodes")
	}

	commands := children[1].GetPayload().(*antlr.BaseParserRuleContext).GetChildren()

	for _, command := range commands {
		if _, ok := command.GetPayload().(*antlr.CommonToken); ok {
			continue
		}
		commandChildren := command.GetPayload().(*antlr.BaseParserRuleContext).GetChildren()

		if len(commandChildren) != 3 {
			log.Fatal("Command must have exactly 3 child nodes")
		}

		fmt.Println("Command:")
		fmt.Printf(" Condition: %v\n", commandChildren[0].
			GetPayload().(*antlr.BaseParserRuleContext).GetText())
		fmt.Printf(" Statement: %v\n", commandChildren[2].
			GetPayload().(*antlr.BaseParserRuleContext).GetText())
	}

	fmt.Println(commands[1].GetPayload().(*antlr.CommonToken).GetText())
}
