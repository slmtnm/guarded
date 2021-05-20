# debug purpose
from guarded.executing_visitor import ExecutingVisitor
from guarded.gen.GuardedLexer import GuardedLexer
from guarded.gen.GuardedParser import GuardedParser
from antlr4 import CommonTokenStream, FileStream

tree = GuardedParser(CommonTokenStream(GuardedLexer(FileStream('examples/macro.gua')))).start()
ExecutingVisitor().visit(tree)