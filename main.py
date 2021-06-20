# debug purpose
from gclang.executing.visitor import Visitor as ExecutingVisitor
from gclang.deriving.visitor import Visitor as DerivingVisitor
from gclang.gen.GuardedLexer import GuardedLexer
from gclang.gen.GuardedParser import GuardedParser
from antlr4 import CommonTokenStream, FileStream

tree = GuardedParser(CommonTokenStream(GuardedLexer(FileStream('examples/arrays/permutation.gua')))).start()
ExecutingVisitor().visit(tree)