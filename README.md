# Guarded

Guarded is the interpreter of Dijkstra's guarded command language,
written in python with ANTLR4 generator.

Example of program in this language:
```
a := 45;
b := 15;

do a != b ->
    if a > b -> a := a - b
    |  a < b -> b := b - a
    fi
od
```

## Quick start:
To start using interpreter, follow these steps:

### With python

* Install all python requirements:
```console
  $ pip install -r requirements.txt
```

* Launch program of your choice with:
```console
  $ python -m guarded run ./examples/euqclid.gua
```