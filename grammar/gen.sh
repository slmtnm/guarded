#!/bin/bash

# Script for generating lexer and parser from
# grammar in 'Guarded.g4' file

cd "$(dirname ${BASH_SOURCE[0]})"
antlr4 -Dlanguage=Python3 -visitor -o ../gclang/gen/ Guarded.g4
