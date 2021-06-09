grammar Guarded;

// Tokens
SEP: ';';
WHITESPACE: [ \r\n\t]+ -> skip;
NUMBER : [0-9]+('.'[0-9]*)?;
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
AND: '&';
OR: '|';
NEG: '~';
IMPL: '>>';
EQUIV: '<=>';

expression
   : functionCall                                           # ExprFnCall
   | arrayLiteral                                           # ExprArrayLiteral
   | arrayElement                                           # ExprArrayElement
   | SUB expression                                         # UnarySub
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
start : initialAssignments? operatorList condition? functionDefinition* EOF;
operatorList: operator (SEP operator)*;

// Operators
operator: assignOperator | ifOperator | doOperator | functionCall;

// assign operator
assignOperator: ID (',' ID)* ':=' expression (',' expression)*;

// Guarded comm ands
commandList: command ('|' command)*;
command: expression '->' operatorList;

ifOperator: 'if' commandList 'fi';
doOperator: condition? 'do' commandList 'od';
condition: '{' expression '}';

// macro-functions
functionCall: ID '(' actualParameters ')';
functionDefinition: ID '(' formalParameters ')' ':=' operatorList;

formalParameters: (ID (',' ID)* )?;
actualParameters: (expression (',' expression)* )?;

initialAssignments: '[' assignOperator (';' assignOperator)* ']';

arrayLiteral: '[' (expression (';' expression)* )? ']';
arrayElement: ID '[' expression ']';

arrayUp: ID ':' 'up' expression;
arrayDown: ID ':' 'down' expression;
arrayUpper: ID ':' 'upper';
arrayLower: ID ':' 'lower';
arraySize: ID ':' 'size';

// comments
LINE_COMMENT
    : '#' ~[\r\n]* -> skip
;