package cmd

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"github.com/spf13/cobra"

	"github.com/antlr/antlr4/runtime/Go/antlr"
	"github.com/slmtnm/secure/parser"
)

var rootCmd = &cobra.Command{
	Use:   "secure <filename>",
	Short: "Interpreter for Dijkstra Secure Commands language",
	Run: func(cmd *cobra.Command, args []string) {
		if len(args) != 1 {
			cmd.Usage()
			fmt.Fprintln(os.Stderr, "Exactly one argument required")
			os.Exit(1)
		}

		filename := args[0]
		content, err := ioutil.ReadFile(filename)

		if err != nil {
			log.Fatal(err)
		}

		is := antlr.NewInputStream(string(content))
		lexer := parser.NewSecureLexer(is)

		listener := &secureListener{}
		stream := antlr.NewCommonTokenStream(lexer, antlr.TokenDefaultChannel)
		p := parser.NewSecureParser(stream)
		antlr.ParseTreeWalkerDefault.Walk(listener, p.Start())

		fmt.Println("Variables:", Vars)
	},
}

//Execute is an entry point
func Execute() {
	rootCmd.Execute()
}
