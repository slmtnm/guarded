import argparse

import antlr4

from .deriving_visitor import DerivingVisitor
from .executing_visitor import ExecutingVisitor
from guarded.gen.GuardedLexer import GuardedLexer
from guarded.gen.GuardedParser import GuardedParser


def parse_arguments() -> (str, str):
    arg_parser = argparse.ArgumentParser(description="Dijkstra's Guarded command language interpreter")
    arg_parser.add_argument('mode', metavar='MODE', type=str, help='mode for interpreter execution')
    arg_parser.add_argument('file', metavar='FILE', type=str, help='file path of script')

    args = arg_parser.parse_args()
    return args.mode, args.file


def main():
    mode, file = parse_arguments()

    text = antlr4.FileStream(file)
    lexer = GuardedLexer(text)
    stream = antlr4.CommonTokenStream(lexer)
    parser = GuardedParser(stream)
    tree = parser.start()
    print()

    if mode == 'run':
        visitor = ExecutingVisitor()
        visitor.visit(tree)

        print('Final state:')
        for var_name, var_value in visitor.vars.items():
            print(f'{var_name} = {var_value}')

    elif mode == 'derive':
        visitor = DerivingVisitor()
        visitor.visit(tree)


main()