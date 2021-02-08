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

// Rules
start : operator (SEP operator)* EOF;
operator: assignOperator | ifOperator;
assignOperator: ID ':=' expression;
ifOperator: 'if' commandList 'fi';
commandList: command ('|' command)*;
command: expression '->' operator;
expression
   : expression op=('*'|'/') expression # MulDiv
   | expression op=('+'|'-') expression # AddSub
   | expression op=('>'|'<'|'>='|'<='|'=='|'!=') expression # Logic
   | NUMBER                             # Number
   ;
