grammar Secure;

// Tokens
SEP: ';';
WHITESPACE: [ \r\n\t]+ -> skip;
NUMBER : [0-9]+;
TRUE: 'True';
FALSE: 'False';
ID : [a-zA-Z_][0-9a-zA-Z_]*;
MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
EQ: '==';
NEQ: '!=';
AND: 'and';
OR: 'or';
NEG: 'not';
IMPL: '=>';
EQUIV: '<=>';

expression
   : SUB expression                                         # UnarySub
   | NEG expression                                         # Negate
   | '(' expression ')'                                     # Brackets
   | expression op=('*'|'/') expression                     # MulDiv
   | expression op=('+'|'-') expression                     # AddSub
   | expression op=('>'|'<'|'>='|'<='|'=='|'!=') expression # Logic
   | expression AND expression                              # And
   | expression OR expression                               # Or
   | expression IMPL expression                             # Impl
   | expression EQUIV expression                            # Equiv
   | NUMBER                                                 # Number
   | ID                                                     # Identifier
   | TRUE                                                   # True
   | FALSE                                                  # False
   ;

// Program is an operator or multiple operators
start : initialState? operatorList postCondition? EOF;
operatorList: operator (SEP operator)*;

// Operators
operator: assignOperator | ifOperator | doOperator;

// assign operator
assignOperator: ID ':=' expression;

// secure commands
commandList: command ('|' command)*;
command: expression '->' operatorList;

ifOperator: 'if' commandList 'fi';
doOperator: 'do' commandList 'od';

// logical programming section
postCondition: '{' expression '}';
initialState: '[' assignOperator (SEP assignOperator)* ']';