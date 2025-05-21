// MSSV: 2212629
// Họ tên: Nguyễn Lê Hoàng Phúc

/* ##########################        OUTLINE        ############################### */

// A. LEXER
//      1. Keywords
//      2. Operators
//      3. Separators
//      4. Identifiers
//      5. Literals
//          5.1. Integer: Decimal, Binary, Octa, Hexa
//          5.2. Floating point
//          5.3. String 
//          5.4. Boolean 
//          5.5. Nil
//      6. Skip
//      7. Comments
//      8. Error
//          8.1. Error characters
//          8.2. Unclosed string 
//          8.3. Illegal escaped

// B. PARSER
//      1. Program definition
//      2. Literals advanced
//          2.1. Array-lit (array instance)
//          2.2. Struct-lit (struct instance)
//      3. Expressions
//      4. Statement
//          4.1. Declare: 
//              4.1.1. variables
//              4.1.2. constants
//              4.1.3. functions
//              4.1.4. methods
//              4.1.5. struct
//              4.1.6. interface
//          4.2. Assignment
//          4.3. If
//          4.4. For
//          4.5. Break
//          4.6. Continue 
//          4.7. Call 
//          4.8. Return

/* ##########################        End - outline      ############################### */

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
prev_token = None

def emit(self):
    tk = self.type

    if tk == self.UNCLOSE_STRING:       
        result = super().emit()
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit()
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(result.text)
    elif tk == self.NEWLINE:
        if self.prev_token and self.prev_token.type in [
            MiniGoLexer.ID, MiniGoLexer.INTEGER_LIT, MiniGoLexer.FLOAT_LIT,
            MiniGoLexer.TRUE, MiniGoLexer.FALSE, MiniGoLexer.STRING_LIT, MiniGoLexer.NIL,
            MiniGoLexer.INT, MiniGoLexer.FLOAT, MiniGoLexer.STRING, MiniGoLexer.BOOLEAN,
            MiniGoLexer.RETURN, MiniGoLexer.CONTINUE, MiniGoLexer.BREAK,
            MiniGoLexer.RPAREN, MiniGoLexer.RBRACK, MiniGoLexer.RBRACE
        ]:
            self.type = MiniGoLexer.SEMICOLON
            self.text = ";"
        else:
            return self.nextToken()

    result = super().emit()
    self.prev_token = result
    return result
}

options{
	language = Python3;
}


/* =========================================================================================== */
///////////////////////////////         L E X E R         ///////////////////////////////////////
/* =========================================================================================== */

// TODO Keywords 3.3.2 pdf --------------------------------------------------------------------------
IF          : 'if';
ELSE        : 'else';
FOR         : 'for';
RETURN      : 'return';
FUNC        : 'func';
TYPE        : 'type';
STRUCT      : 'struct';
INTERFACE   : 'interface';
STRING      : 'string';
INT         : 'int';
FLOAT       : 'float';
BOOLEAN     : 'boolean';
CONST       : 'const';
VAR         : 'var';
CONTINUE    : 'continue';
BREAK       : 'break';
RANGE       : 'range';
NIL         : 'nil';
TRUE        : 'true';
FALSE       : 'false';

NEWLINE     : '\r'? '\n';

//TODO Operators 3.3.3 pdf --------------------------------------------------------------------------
ADD         : '+';
SUB         : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%';

EQUAL       : '==';
NOT_EQUAL   : '!=';
LESS        : '<';
LESS_EQUAL  : '<=';
GREATER     : '>';
GREATER_EQUAL: '>=';

AND         : '&&';
OR          : '||';
NOT         : '!';

ASSIGN      : '=';
ASSIGN_STATE: ':=';
ADD_ASSIGN  : '+=';
SUB_ASSIGN  : '-=';
MUL_ASSIGN  : '*=';
DIV_ASSIGN  : '/=';
MOD_ASSIGN  : '%=';

DOT         : '.';

//TODO Separators 3.3.4 pdf --------------------------------------------------------------------------
LPAREN      : '(';
RPAREN      : ')';
LBRACE      : '{';
RBRACE      : '}';
LBRACK      : '[';
RBRACK      : ']';
COMMA       : ',';
SEMICOLON   : ';';
COLON       : ':';

//TODO Identifiers 3.3.1 pdf --------------------------------------------------------------------------
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

//TODO Literals 3.3.5 pdf --------------------------------------------------------------------------
INTEGER_LIT : DEC | BIN | OCT | HEX;
    // : DEC
    // | BIN {self.text = str(int(self.text, 2));} 
    // | OCT {self.text = str(int(self.text, 8));} 
    // | HEX {self.text = str(int(self.text, 16));};
    fragment DEC: '0' | [1-9] [0-9]* ;
    fragment BIN: ('0b'|'0B') [0-1]+;
    fragment OCT: ('0o'|'0O') [0-7]+;
    fragment HEX: ('0x'|'0X') [0-9a-fA-F]+; 

FLOAT_LIT               
    : REAL_NUM (EXPONENT_PART)?;
    fragment REAL_NUM       : [0-9]+ '.' [0-9]*;
    fragment EXPONENT_PART  : [eE] [+-]? [0-9]+;

STRING_LIT              
    : '"' CHARACTER* '"';
    fragment CHARACTER  : (~["\\\r\n] | ESCAPED_SEQ);
    fragment ESCAPED_SEQ: '\\n' | '\\t' | '\\r' | '\\"' |'\\\\';    // hoặc: fragment ESCAPED_SEQ: [\n\t\r\"\\];

//TODO skip 3.1 and 3.2 pdf --------------------------------------------------------------------------
WS: [ \t\f\r]+ -> skip;                                             // (Xem TOKEN: NEWLINE)

//TODO Comment 3.2 pdf --------------------------------------------------------------------------
COMMENT_INLINE  : '//' (~[\n\r])* -> skip;
COMMENT_BLOCK   : '/*' ( COMMENT_BLOCK | COMMENT_INLINE | (.) )*? '*/' -> skip;

//TODO ERROR pdf BTL1 + lexererr.py -------------------------------------------------------------------
ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' CHARACTER* ('\r\n' | '\n' | EOF) { 
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[:-1])
    else:
        raise UncloseString(self.text)
};

ILLEGAL_ESCAPE: '"' CHARACTER* ESC_ILLEGAL {
    raise IllegalEscape(self.text)
};
fragment ESC_ILLEGAL: [\r] | '\\' ~[ntr"\\];

/*----------------------------------       END LEXER       ------------------------------------ */
/* =========================================================================================== */




/* =========================================================================================== */
///////////////////////////////         P A S E R          //////////////////////////////////////
/* =========================================================================================== */

// Program definition --------------------------------------------------------------------------
program: declared_statement_list EOF;

declared_statement_list: (declared_statement) (declared_statement_list) | (declared_statement);

//TODO Literal 6.6 pdf --------------------------------------------------------------------------
literal:
	literal_primitive
	| array_lit_instance
	| struct_lit_instance;

literal_primitive: 
    INTEGER_LIT
	| FLOAT_LIT
	| STRING_LIT
    | TRUE
    | FALSE
    | NIL;

mytype: ID | primitive_type | array_type;
    primitive_type  : INT | FLOAT | BOOLEAN | STRING;
    array_type      : (array_dimention) (ID | primitive_type);
    array_dimention : (array_dimention_element) (array_dimention) | array_dimention_element;
    array_dimention_element: LBRACK (INTEGER_LIT | ID) RBRACK;

array_lit_instance: array_type LBRACE list_array_value RBRACE;              // Array_type + giá trị // Example:  [2][3]int {{1,2,3}, {4,5,6}
    list_array_value: (list_array_value_element) COMMA (list_array_value) | (list_array_value_element);
    list_array_value_element: ID 
                            | literal_primitive 
                            | struct_lit_instance 
                            | LBRACE list_array_value RBRACE;
    
struct_lit_instance: ID LBRACE struct_lit_instance_body RBRACE;              // Struct_type + giá trị // Example:   Person{name: "Alice", age: 30}  
    struct_lit_instance_body        : struct_lit_instance_body_prime | ;
    struct_lit_instance_body_prime  : struct_lit_instance_body_element COMMA struct_lit_instance_body_prime | struct_lit_instance_body_element;
    struct_lit_instance_body_element: ID COLON expression;

// TODO 5.2 Expressions 6 pdf ---------------------------------------------------------------------
list_expression: list_expression_prime | ;
list_expression_prime: expression COMMA list_expression_prime | expression;
    expression : expression OR expression1 | expression1;
    expression1 : expression1 AND           expression2 | expression2;
    expression2 : expression2 EQUAL         expression3
                | expression2 NOT_EQUAL     expression3
                | expression2 LESS          expression3
                | expression2 LESS_EQUAL    expression3
                | expression2 GREATER       expression3
                | expression2 GREATER_EQUAL expression3
                | expression3;
    expression3 : expression3 ADD expression4
                | expression3 SUB expression4
                | expression4;
    expression4 : expression4 MUL expression5
                | expression4 DIV expression5
                | expression4 MOD expression5
                | expression5;
    expression5 : NOT expression5
                | SUB expression5
                | expression6;
    expression6 : expression6 (LBRACK expression RBRACK)                    // 6.4 pdf --> Accessing array elements. VD:  a[2][3], b[4] ...
                | expression6 DOT ID                                        // 6.5 pdf --> Accessing struct fields. VD:  person.name,  person.age.b ...
                | expression6 DOT (function_call)                           // Method call //person.age.b.a()
                | function_call                                             // Function call
                | ID 
                | literal
                | expression7;
    expression7 : LPAREN expression RPAREN;
                
    function_call: ID LPAREN list_expression RPAREN;                        // 6.7.1 Function call
    method_call  : temp_expression6 DOT (function_call);                    // 6.7.2 Method call

    temp_expression6: temp_expression6 (LBRACK expression RBRACK)                    
                    | temp_expression6 DOT ID                                        
                    | temp_expression6 DOT function_call
                    | function_call
                    | ID;


//TODO Statement 5 and 4 pdf ----------------------------------------------------------------------
list_statement: list_statement_prime | ;
list_statement_prime: statement (list_statement_prime) | statement;

statement   
    : declared_statement
    | assignment_statement
    | if_statement
    | for_statement
    | break_statement
    | continue_statement
    | call_statement
    | return_statement;


//TODO declared_statement --------------------------------------------------------------------------
declared_statement                          
    : variables_declared                    
    | constants_declared                    
    | function_declared
    | method_declared
    | struct_declared
    | interface_declared;

variables_declared: VAR ID ((mytype ASSIGN expression) | mytype | ASSIGN expression) SEMICOLON;
variables_declared_without_semi_for_loop: VAR ID mytype? ASSIGN expression;

constants_declared: CONST ID ASSIGN expression SEMICOLON;

function_declared: FUNC ID (LPAREN list_function_parameter RPAREN) (mytype)? (function_body_container) SEMICOLON;
    list_function_parameter          : list_function_parameter_prime | ;
    list_function_parameter_prime    : list_function_parameter_element COMMA list_function_parameter_prime | list_function_parameter_element;
    list_function_parameter_element  : ID (COMMA ID)* (mytype);
    function_body_container: LBRACE list_statement_prime RBRACE;

method_declared: FUNC (receiver_container) ID (LPAREN list_function_parameter RPAREN) (mytype)? (function_body_container) SEMICOLON;
    receiver_container: LPAREN ID ID RPAREN;

struct_declared: TYPE ID STRUCT (LBRACE struct_declared_body RBRACE) SEMICOLON;
    struct_declared_body        : (struct_declared_body_element) (struct_declared_body) | (struct_declared_body_element);
    struct_declared_body_element: ID (mytype) SEMICOLON;
 
interface_declared: TYPE ID INTERFACE (LBRACE interface_declared_body RBRACE) SEMICOLON;
    interface_declared_body     : (interface_declared_element) (interface_declared_body) | (interface_declared_element);
    interface_declared_element  : ID (interface_parameter_container) (mytype)? SEMICOLON;
    interface_parameter_container     : LPAREN list_interface_parameter RPAREN;
    list_interface_parameter          : list_interface_parameter_prime | ;
    list_interface_parameter_prime    : list_interface_parameter_element COMMA list_interface_parameter_prime | list_interface_parameter_element;
    list_interface_parameter_element  : ID (COMMA ID)* (mytype);


//TODO assign_statement --------------------------------------------------------------------------
assignment_statement: (lhs_assignment_statement) (assignment_operator) (expression) SEMICOLON;
    assignment_operator: ASSIGN_STATE | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
    lhs_assignment_statement: ID
                            | lhs_assignment_statement (LBRACK expression RBRACK)
                            | lhs_assignment_statement DOT ID;

    assignment_statement_without_semi_for_loop: ID (assignment_operator) (expression);

// TODO if_statement: --------------------------------------------------------------------------
if_statement: IF (LPAREN expression RPAREN) (function_body_container) (else_if_clause)? (else_clause)? SEMICOLON;
    else_if_clause : (else_if_clause_content) else_if_clause | (else_if_clause_content);
    else_if_clause_content: ELSE IF (LPAREN expression RPAREN) (function_body_container);

    else_clause: ELSE function_body_container;

// TODO for_statement: --------------------------------------------------------------------------
for_statement: (array_for_loop | initialization_for_loop | basic_for_loop) SEMICOLON;
    basic_for_loop: FOR expression (function_body_container);
    initialization_for_loop: FOR (variables_declared_without_semi_for_loop | assignment_statement_without_semi_for_loop) 
                            SEMICOLON (expression) 
                            SEMICOLON (assignment_statement_without_semi_for_loop)
                            (function_body_container);
    array_for_loop: FOR (ID) COMMA (ID ASSIGN_STATE RANGE expression) (function_body_container);

// TODO break_statement: ------------------------------------------------------------------------
break_statement: BREAK SEMICOLON;

// TODO continue_statement: ---------------------------------------------------------------------
continue_statement: CONTINUE SEMICOLON;

// TODO call_statement: --------------------------------------------------------------------------
call_statement: (function_call | method_call) SEMICOLON;

// TODO return_statement: ------------------------------------------------------------------------
return_statement: RETURN expression? SEMICOLON;


/*----------------------------------       END PARSER       ------------------------------------ */
/* ============================================================================================= */