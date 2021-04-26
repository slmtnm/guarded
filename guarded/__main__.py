import click

from .deriving_visitor import DerivingVisitor
from .executing_visitor import ExecutingVisitor
from guarded.gen.GuardedLexer import GuardedLexer
from guarded.gen.GuardedParser import GuardedParser

from antlr4 import CommonTokenStream, FileStream


@click.group(help='Guarded command language interpreter')
@click.version_option(prog_name='guarded')
def cli():
    ...


@cli.command(help='Run program and print final state')
@click.argument('file')
def run(file):
    ast = GuardedParser(CommonTokenStream(GuardedLexer(FileStream(file)))).start()
    ExecutingVisitor().visit(ast)


@cli.command(help='Derive initial state from specified final state')
@click.argument('file')
def derive(file):
    ast = GuardedParser(CommonTokenStream(GuardedLexer(FileStream(file)))).start()
    DerivingVisitor().visit(ast)


if __name__ == '__main__':
    cli()