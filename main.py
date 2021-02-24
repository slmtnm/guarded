import sys
import antlr4
from gen.SecureLexer import SecureLexer
from gen.SecureParser import SecureParser
from visitor import MySecureVisitor


def main():
    text = antlr4.FileStream(sys.argv[1])
    lexer = SecureLexer(text)
    stream = antlr4.CommonTokenStream(lexer)
    parser = SecureParser(stream)
    tree = parser.start()
    visitor = MySecureVisitor()
    visitor.visit(tree)

    print(f"Stack: {visitor.stack}")
    print(f"Vars: {visitor.vars}")


if __name__ == '__main__':
    main()
