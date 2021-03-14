import sys
import antlr4
from gen.SecureLexer import SecureLexer
from gen.SecureParser import SecureParser
from visitor import MySecureVisitor

'''
    Interpreter can be executed in 3 exclusive modes:
        * run - executing program, and asserting if
          post-condition is false

        * analyze - do not execute program, but derive
          pre-condition from post-condition

        * combine - first perform analyzing, then
          check that input data satisfy pre-condition (assert if not),
          and then execute program. Checking post-condition is not
          necessery.

    Start state can be defined in separate file, or from stdin.
    In program code you just define what are names of variables,
    that belong to start state.
'''

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
