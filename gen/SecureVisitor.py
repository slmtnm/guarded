# Generated from Secure.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SecureParser import SecureParser
else:
    from SecureParser import SecureParser

# This class defines a complete generic visitor for a parse tree produced by SecureParser.

class SecureVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SecureParser#Identifier.
    def visitIdentifier(self, ctx:SecureParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#Or.
    def visitOr(self, ctx:SecureParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#Brackets.
    def visitBrackets(self, ctx:SecureParser.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#Number.
    def visitNumber(self, ctx:SecureParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#MulDiv.
    def visitMulDiv(self, ctx:SecureParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#AddSub.
    def visitAddSub(self, ctx:SecureParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#And.
    def visitAnd(self, ctx:SecureParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#UnarySub.
    def visitUnarySub(self, ctx:SecureParser.UnarySubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#True.
    def visitTrue(self, ctx:SecureParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#Negate.
    def visitNegate(self, ctx:SecureParser.NegateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#False.
    def visitFalse(self, ctx:SecureParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#Logic.
    def visitLogic(self, ctx:SecureParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#start.
    def visitStart(self, ctx:SecureParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#operatorList.
    def visitOperatorList(self, ctx:SecureParser.OperatorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#operator.
    def visitOperator(self, ctx:SecureParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#assignOperator.
    def visitAssignOperator(self, ctx:SecureParser.AssignOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#commandList.
    def visitCommandList(self, ctx:SecureParser.CommandListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#command.
    def visitCommand(self, ctx:SecureParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#ifOperator.
    def visitIfOperator(self, ctx:SecureParser.IfOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SecureParser#doOperator.
    def visitDoOperator(self, ctx:SecureParser.DoOperatorContext):
        return self.visitChildren(ctx)



del SecureParser