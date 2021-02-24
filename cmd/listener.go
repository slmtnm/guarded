package cmd

import (
	"fmt"
	"log"

	"github.com/slmtnm/secure/parser"

	"github.com/antlr/antlr4/runtime/Go/antlr"
)

// Listener is main secureListener instance
var Listener secureListener

func init() {
	newStack := Stack(make([]interface{}, 0))

	Listener.vars = make(map[string]interface{})
	Listener.stack = &newStack
}

type secureListener struct {
	*parser.BaseSecureListener

	stack *Stack
	vars  map[string]interface{}
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
	varValue := l.stack.pop()

	l.vars[varName] = varValue
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
}
