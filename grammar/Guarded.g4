grammar Guarded;

// Tokens
SEP: ';';
WHITESPACE: [ \r\n\t]+ -> skip;
NUMBER : [0-9]+('.'[0-9]*)?;
TRUE: 'True';
FALSE: 'False';
LOCAL_VARIABLE: 'local';
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
AND: '&&';
OR: '||';
NEG: '~';
IMPL: '>>';
EQUIV: '<=>';
LOWER_BOUND_DELIMITER: '|';


expression
    : ID '(' actualParameters ')'                            # ExprMacroCall
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
    | '[' (expression LOWER_BOUND_DELIMITER)? (expression (',' expression)*)? ']'  # ArrayLiteral
    | NUMBER                                                 # Number
    | ID                                                     # Identifier
    | TRUE                                                   # True
    | FALSE                                                  # False
    | arrayLowerBound                                        # ExprArrayLowerBound
    | arrayUpperBound                                        # ExprArrayUpperBound
    | arraySize                                              # ExprArraySize
    | arrayElement                                           # ExprArrayElement
    | arrayLowerElement                                      # ExprArrayLowerElement
    | arrayUpperElement                                      # ExprArrayUpperElement
    ;

// Program is an operator or multiple operators (or expression for repl)
start
    : expression
    | initialAssignments? operatorList condition? macroOperatorDefinition* EOF
    ;
operatorList: (operator (SEP operator)*)?;

// Operators
operator
    : skipOperator
    | abortOperator
    | assignOperator
    | macroExpressionDefinition
    | ifOperator
    | doOperator
    | macroCall
    | arraySet
    | arraySwap
    | arrayPopUp
    | arrayPopDown
    | arrayDelUp
    | arrayDelDown
    | arrayPushUp
    | arrayPushDown
    | arrayShift
    | printOperator
    ;

skipOperator: 'skip';
abortOperator: 'abort';
printOperator: 'print' expression;

// assign operator
assignOperator: (LOCAL_VARIABLE)? ID (',' ID)* ':=' expression (',' expression)*;

// Guarded comm ands
commandList: command ('|' command)*;
command: expression '->' operatorList;

ifOperator: 'if' commandList 'fi';
doOperator: condition? 'do' commandList 'od';
condition: '{' expression '}';

// macro operators
macroCall: ID '(' actualParameters ')';
macroOperatorDefinition: ID '(' formalParameters ')' '{' operatorList '}';
macroExpressionDefinition: ID '(' formalParameters ')' ':=' expression;

formalParameters: (ID (',' ID)* )?;
actualParameters: (expression (',' expression)* )?;

initialAssignments: '[' assignOperator (';' assignOperator)* ']';

// arrays
arrayLowerBound: ID '.lowb';
arrayUpperBound: ID '.upb';
arraySize: ID '.size';
arrayElement: ID '[' expression ']';
arrayLowerElement: ID '.lower';
arrayUpperElement: ID '.upper';
arrayShift: ID ':shift' '(' expression ')';
arrayPushUp: ID ':pushup' '(' expression ')';
arrayPushDown: ID ':pushdown' '(' expression ')';
arrayDelUp: ID ':delup';
arrayDelDown: ID ':deldown';
arrayPopUp: ID ',' ID ':popup';
arrayPopDown: ID ',' ID ':popdown';
arraySwap: ID ':swap' '(' expression ',' expression ')';
arraySet: ID ':' '[' expression ']' '=' expression;
// arrayLiteral: '(' expression (',' expression)* ')';

// comments
LINE_COMMENT
    : '#' ~[\r\n]* -> skip
;