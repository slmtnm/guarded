// Code generated from Secure.g4 by ANTLR 4.9.1. DO NOT EDIT.

package parser // Secure

import "github.com/antlr/antlr4/runtime/Go/antlr"

// BaseSecureListener is a complete listener for a parse tree produced by SecureParser.
type BaseSecureListener struct{}

var _ SecureListener = &BaseSecureListener{}

// VisitTerminal is called when a terminal node is visited.
func (s *BaseSecureListener) VisitTerminal(node antlr.TerminalNode) {}

// VisitErrorNode is called when an error node is visited.
func (s *BaseSecureListener) VisitErrorNode(node antlr.ErrorNode) {}

// EnterEveryRule is called when any rule is entered.
func (s *BaseSecureListener) EnterEveryRule(ctx antlr.ParserRuleContext) {}

// ExitEveryRule is called when any rule is exited.
func (s *BaseSecureListener) ExitEveryRule(ctx antlr.ParserRuleContext) {}

// EnterIdentifier is called when production Identifier is entered.
func (s *BaseSecureListener) EnterIdentifier(ctx *IdentifierContext) {}

// ExitIdentifier is called when production Identifier is exited.
func (s *BaseSecureListener) ExitIdentifier(ctx *IdentifierContext) {}

// EnterNumber is called when production Number is entered.
func (s *BaseSecureListener) EnterNumber(ctx *NumberContext) {}

// ExitNumber is called when production Number is exited.
func (s *BaseSecureListener) ExitNumber(ctx *NumberContext) {}

// EnterMulDiv is called when production MulDiv is entered.
func (s *BaseSecureListener) EnterMulDiv(ctx *MulDivContext) {}

// ExitMulDiv is called when production MulDiv is exited.
func (s *BaseSecureListener) ExitMulDiv(ctx *MulDivContext) {}

// EnterAddSub is called when production AddSub is entered.
func (s *BaseSecureListener) EnterAddSub(ctx *AddSubContext) {}

// ExitAddSub is called when production AddSub is exited.
func (s *BaseSecureListener) ExitAddSub(ctx *AddSubContext) {}

// EnterLogic is called when production Logic is entered.
func (s *BaseSecureListener) EnterLogic(ctx *LogicContext) {}

// ExitLogic is called when production Logic is exited.
func (s *BaseSecureListener) ExitLogic(ctx *LogicContext) {}

// EnterStart is called when production start is entered.
func (s *BaseSecureListener) EnterStart(ctx *StartContext) {}

// ExitStart is called when production start is exited.
func (s *BaseSecureListener) ExitStart(ctx *StartContext) {}

// EnterOperatorList is called when production operatorList is entered.
func (s *BaseSecureListener) EnterOperatorList(ctx *OperatorListContext) {}

// ExitOperatorList is called when production operatorList is exited.
func (s *BaseSecureListener) ExitOperatorList(ctx *OperatorListContext) {}

// EnterOperator is called when production operator is entered.
func (s *BaseSecureListener) EnterOperator(ctx *OperatorContext) {}

// ExitOperator is called when production operator is exited.
func (s *BaseSecureListener) ExitOperator(ctx *OperatorContext) {}

// EnterAssignOperator is called when production assignOperator is entered.
func (s *BaseSecureListener) EnterAssignOperator(ctx *AssignOperatorContext) {}

// ExitAssignOperator is called when production assignOperator is exited.
func (s *BaseSecureListener) ExitAssignOperator(ctx *AssignOperatorContext) {}

// EnterCommandList is called when production commandList is entered.
func (s *BaseSecureListener) EnterCommandList(ctx *CommandListContext) {}

// ExitCommandList is called when production commandList is exited.
func (s *BaseSecureListener) ExitCommandList(ctx *CommandListContext) {}

// EnterCommand is called when production command is entered.
func (s *BaseSecureListener) EnterCommand(ctx *CommandContext) {}

// ExitCommand is called when production command is exited.
func (s *BaseSecureListener) ExitCommand(ctx *CommandContext) {}

// EnterIfOperator is called when production ifOperator is entered.
func (s *BaseSecureListener) EnterIfOperator(ctx *IfOperatorContext) {}

// ExitIfOperator is called when production ifOperator is exited.
func (s *BaseSecureListener) ExitIfOperator(ctx *IfOperatorContext) {}
