#!/bin/bash

# Script for generating ANTLR parser for Go language,
# with grammar specified in Secure.g4 file.

antlr4 -Dlanguage=Go -o parser Secure.g4