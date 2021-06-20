import click

from .deriving.visitor import Visitor as DerivingVisitor
from .executing.visitor import Visitor as ExecutingVisitor
from .translate.latex_visitor import LatexVisitor
from .translate.python_visitor import PythonVisitor
from .gen.GuardedLexer import GuardedLexer
from .gen.GuardedParser import GuardedParser
import sys

from antlr4 import CommonTokenStream, FileStream


@click.group(help='Guarded command language interpreter')
@click.version_option(prog_name='guarded')
@click.argument('file')
@click.pass_context
def cli(ctx, file):
    ctx.obj = GuardedParser(CommonTokenStream(
        GuardedLexer(FileStream(file)))).start()


@cli.command(help='Run program and print final state')
@click.pass_context
def run(ctx):
    for k, v in ExecutingVisitor().visit(ctx.obj).items():
        print(f'{k} = {v}')


@cli.command(help='Derive initial state from specified final state')
@click.pass_context
def derive(ctx):
    DerivingVisitor().visit(ctx.obj)


@cli.group(help='Translate guarded program to other language')
def translate():
    ...


@translate.command()
@click.pass_context
def latex(ctx):
    print(LatexVisitor().visit(ctx.obj))


@translate.command()
@click.pass_context
def python(ctx):
    PythonVisitor().visit(ctx.obj)


if __name__ == '__main__':
    cli()
