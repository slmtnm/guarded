import sys

import click
from antlr4 import CommonTokenStream, FileStream, InputStream

from gclang.guarded_exception import GuardedException

from .deriving.reverse_visitor import ReverseVisitor as DerivingVisitor
from .executing.visitor import Visitor as ExecutingVisitor
from .gen.GuardedLexer import GuardedLexer
from .gen.GuardedParser import GuardedParser
from .translate.latex_visitor import LatexVisitor
from .translate.python_visitor import PythonVisitor

def build_tree(file):
    return GuardedParser(CommonTokenStream(GuardedLexer(FileStream(file)))).start()

@click.group(help='Guarded command language interpreter')
@click.version_option(prog_name='guarded')
@click.pass_context
def cli(ctx):
    pass

@cli.command(help='Run program and print final state')
@click.pass_context
@click.argument('file')
@click.option('--verbose', '-v', is_flag=True, help='Print result state')
def run(ctx, file, verbose):
    try:
        result = ExecutingVisitor().visit(build_tree(file))
        if verbose:
            print('Final state:')
            for k, v in result.items():
                print(f'{k} = {v}')
    except GuardedException as e:
        sys.stderr.write(str(e) + '\n')
        exit(1)


@cli.command(help='Derive initial state from specified final state')
@click.argument('file')
@click.pass_context
def derive(ctx, file):
    DerivingVisitor().visit(build_tree(file))


@cli.group(help='Translate guarded program to other language')
def translate():
    ...


@translate.command()
@click.argument('file')
@click.pass_context
def latex(ctx, file):
    print(LatexVisitor().visit(build_tree(file)))


@translate.command()
@click.argument('file')
@click.pass_context
def python(ctx, file):
    PythonVisitor().visit(ctx.obj)

@cli.command(name='repl', help='REPL for guarded command language')
def repl():
    visitor = ExecutingVisitor()
    while True:
        line = input('>>> ')
        try:
            tree = GuardedParser(CommonTokenStream(GuardedLexer(InputStream(line)))).start()
            result = visitor.visit(tree)

            if 'ans' in result:
                print(result['ans'])
        except BaseException as e:
            print('Error: ' + str(e))

if __name__ == '__main__':
    cli()
