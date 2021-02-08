// Code generated from Secure.g4 by ANTLR 4.9.1. DO NOT EDIT.

package parser // Secure

import "github.com/antlr/antlr4/runtime/Go/antlr"

// SecureListener is a complete listener for a parse tree produced by SecureParser.
type SecureListener interface {
	antlr.ParseTreeListener

	// EnterStart is called when entering the start production.
	EnterStart(c *StartContext)

	// EnterOperator is called when entering the operator production.
	EnterOperator(c *OperatorContext)

	// EnterAssignOperator is called when entering the assignOperator production.
	EnterAssignOperator(c *AssignOperatorContext)

	// EnterIfOperator is called when entering the ifOperator production.
	EnterIfOperator(c *IfOperatorContext)

	// EnterCommandList is called when entering the commandList production.
	EnterCommandList(c *CommandListContext)

	// EnterCommand is called when entering the command production.
	EnterCommand(c *CommandContext)

	// EnterNumber is called when entering the Number production.
	EnterNumber(c *NumberContext)

	// EnterMulDiv is called when entering the MulDiv production.
	EnterMulDiv(c *MulDivContext)

	// EnterAddSub is called when entering the AddSub production.
	EnterAddSub(c *AddSubContext)

	// EnterLogic is called when entering the Logic production.
	EnterLogic(c *LogicContext)

	// ExitStart is called when exiting the start production.
	ExitStart(c *StartContext)

	// ExitOperator is called when exiting the operator production.
	ExitOperator(c *OperatorContext)

	// ExitAssignOperator is called when exiting the assignOperator production.
	ExitAssignOperator(c *AssignOperatorContext)

	// ExitIfOperator is called when exiting the ifOperator production.
	ExitIfOperator(c *IfOperatorContext)

	// ExitCommandList is called when exiting the commandList production.
	ExitCommandList(c *CommandListContext)

	// ExitCommand is called when exiting the command production.
	ExitCommand(c *CommandContext)

	// ExitNumber is called when exiting the Number production.
	ExitNumber(c *NumberContext)

	// ExitMulDiv is called when exiting the MulDiv production.
	ExitMulDiv(c *MulDivContext)

	// ExitAddSub is called when exiting the AddSub production.
	ExitAddSub(c *AddSubContext)

	// ExitLogic is called when exiting the Logic production.
	ExitLogic(c *LogicContext)
}
