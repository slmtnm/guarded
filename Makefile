all: build

build: parser
	go build .

parser:
	go generate
