package main

import (
	"github.com/slmtnm/secure/cmd"
)

//go:generate antlr4 -Dlanguage=Go -o parser Secure.g4
func main() {
	cmd.Execute()
}
