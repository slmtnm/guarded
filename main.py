# debug purpose
from gclang.executing_visitor import ExecutingVisitor
from gclang.deriving_visitor import DerivingVisitor
from gclang.gen.GuardedLexer import GuardedLexer
from gclang.gen.GuardedParser import GuardedParser
from antlr4 import CommonTokenStream, FileStream

tree = GuardedParser(CommonTokenStream(GuardedLexer(FileStream('examples/euqclid.gua')))).start()
DerivingVisitor().visit(tree)