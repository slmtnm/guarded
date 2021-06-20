# debug purpose
from gclang.executing.visitor import Visitor as ExecutingVisitor
from gclang.deriving.reverse_visitor import ReverseVisitor as DerivingVisitor
from gclang.gen.GuardedLexer import GuardedLexer
from gclang.gen.GuardedParser import GuardedParser
from antlr4 import CommonTokenStream, FileStream

tree = GuardedParser(CommonTokenStream(GuardedLexer(FileStream('examples/macro.gua')))).start()
DerivingVisitor().visit(tree)