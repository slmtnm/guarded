#!/bin/bash

cd "$(dirname ${BASH_SOURCE[0]})"
antlr4 -Dlanguage=Python3 -visitor -o ../guarded/gen/ Guarded.g4
cd -