grammar Secure;

// Tokens
SEP: ';';
WHITESPACE: [ \r\n\t]+ -> skip;
NUMBER : [1-9][0-9]*;
ID : [a-zA-Z_][a-zA-Z]*;
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

expression
   : expression op=('*'|'/') expression                     # MulDiv
   | expression op=('+'|'-') expression                     # AddSub
   | expression op=('>'|'<'|'>='|'<='|'=='|'!=') expression # Logic
   | NUMBER                                                 # Number
   | ID                                                     # Identifier
   ;

// Program is an operator or multiple operators
start : operatorList EOF;
operatorList: operator (SEP operator)*;

// Operators
operator: assignOperator | ifOperator;

// assign operator
assignOperator: ID ':=' expression;

// secure commands
commandList: command ('|' command)*;
command: expression '->' operator;

ifOperator: 'if' commandList 'fi';
doOperator: 'do' commandList 'od';
