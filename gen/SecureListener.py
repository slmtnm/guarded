# Generated from Secure.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SecureParser import SecureParser
else:
    from SecureParser import SecureParser

# This class defines a complete listener for a parse tree produced by SecureParser.
class SecureListener(ParseTreeListener):

    # Enter a parse tree produced by SecureParser#Identifier.
    def enterIdentifier(self, ctx:SecureParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SecureParser#Identifier.
    def exitIdentifier(self, ctx:SecureParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SecureParser#Or.
    def enterOr(self, ctx:SecureParser.OrContext):
        pass

    # Exit a parse tree produced by SecureParser#Or.
    def exitOr(self, ctx:SecureParser.OrContext):
        pass


    # Enter a parse tree produced by SecureParser#Brackets.
    def enterBrackets(self, ctx:SecureParser.BracketsContext):
        pass

    # Exit a parse tree produced by SecureParser#Brackets.
    def exitBrackets(self, ctx:SecureParser.BracketsContext):
        pass


    # Enter a parse tree produced by SecureParser#Number.
    def enterNumber(self, ctx:SecureParser.NumberContext):
        pass

    # Exit a parse tree produced by SecureParser#Number.
    def exitNumber(self, ctx:SecureParser.NumberContext):
        pass


    # Enter a parse tree produced by SecureParser#MulDiv.
    def enterMulDiv(self, ctx:SecureParser.MulDivContext):
        pass

    # Exit a parse tree produced by SecureParser#MulDiv.
    def exitMulDiv(self, ctx:SecureParser.MulDivContext):
        pass


    # Enter a parse tree produced by SecureParser#AddSub.
    def enterAddSub(self, ctx:SecureParser.AddSubContext):
        pass

    # Exit a parse tree produced by SecureParser#AddSub.
    def exitAddSub(self, ctx:SecureParser.AddSubContext):
        pass


    # Enter a parse tree produced by SecureParser#And.
    def enterAnd(self, ctx:SecureParser.AndContext):
        pass

    # Exit a parse tree produced by SecureParser#And.
    def exitAnd(self, ctx:SecureParser.AndContext):
        pass


    # Enter a parse tree produced by SecureParser#UnarySub.
    def enterUnarySub(self, ctx:SecureParser.UnarySubContext):
        pass

    # Exit a parse tree produced by SecureParser#UnarySub.
    def exitUnarySub(self, ctx:SecureParser.UnarySubContext):
        pass


    # Enter a parse tree produced by SecureParser#True.
    def enterTrue(self, ctx:SecureParser.TrueContext):
        pass

    # Exit a parse tree produced by SecureParser#True.
    def exitTrue(self, ctx:SecureParser.TrueContext):
        pass


    # Enter a parse tree produced by SecureParser#Negate.
    def enterNegate(self, ctx:SecureParser.NegateContext):
        pass

    # Exit a parse tree produced by SecureParser#Negate.
    def exitNegate(self, ctx:SecureParser.NegateContext):
        pass


    # Enter a parse tree produced by SecureParser#False.
    def enterFalse(self, ctx:SecureParser.FalseContext):
        pass

    # Exit a parse tree produced by SecureParser#False.
    def exitFalse(self, ctx:SecureParser.FalseContext):
        pass


    # Enter a parse tree produced by SecureParser#Logic.
    def enterLogic(self, ctx:SecureParser.LogicContext):
        pass

    # Exit a parse tree produced by SecureParser#Logic.
    def exitLogic(self, ctx:SecureParser.LogicContext):
        pass


    # Enter a parse tree produced by SecureParser#start.
    def enterStart(self, ctx:SecureParser.StartContext):
        pass

    # Exit a parse tree produced by SecureParser#start.
    def exitStart(self, ctx:SecureParser.StartContext):
        pass


    # Enter a parse tree produced by SecureParser#operatorList.
    def enterOperatorList(self, ctx:SecureParser.OperatorListContext):
        pass

    # Exit a parse tree produced by SecureParser#operatorList.
    def exitOperatorList(self, ctx:SecureParser.OperatorListContext):
        pass


    # Enter a parse tree produced by SecureParser#operator.
    def enterOperator(self, ctx:SecureParser.OperatorContext):
        pass

    # Exit a parse tree produced by SecureParser#operator.
    def exitOperator(self, ctx:SecureParser.OperatorContext):
        pass


    # Enter a parse tree produced by SecureParser#assignOperator.
    def enterAssignOperator(self, ctx:SecureParser.AssignOperatorContext):
        pass

    # Exit a parse tree produced by SecureParser#assignOperator.
    def exitAssignOperator(self, ctx:SecureParser.AssignOperatorContext):
        pass


    # Enter a parse tree produced by SecureParser#commandList.
    def enterCommandList(self, ctx:SecureParser.CommandListContext):
        pass

    # Exit a parse tree produced by SecureParser#commandList.
    def exitCommandList(self, ctx:SecureParser.CommandListContext):
        pass


    # Enter a parse tree produced by SecureParser#command.
    def enterCommand(self, ctx:SecureParser.CommandContext):
        pass

    # Exit a parse tree produced by SecureParser#command.
    def exitCommand(self, ctx:SecureParser.CommandContext):
        pass


    # Enter a parse tree produced by SecureParser#ifOperator.
    def enterIfOperator(self, ctx:SecureParser.IfOperatorContext):
        pass

    # Exit a parse tree produced by SecureParser#ifOperator.
    def exitIfOperator(self, ctx:SecureParser.IfOperatorContext):
        pass


    # Enter a parse tree produced by SecureParser#doOperator.
    def enterDoOperator(self, ctx:SecureParser.DoOperatorContext):
        pass

    # Exit a parse tree produced by SecureParser#doOperator.
    def exitDoOperator(self, ctx:SecureParser.DoOperatorContext):
        pass



del SecureParser