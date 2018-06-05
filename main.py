from exceptions.error import PlyError
from exceptions.internalerror import PlyInternalError
from exceptions.rangeerror import PlyRangeError
from exceptions.syntaxerror import PlySyntaxError
from exceptions.typeerror import PlyTypeError

from runtime import runtime

reserved = {
    "if"  : "IF",
    "then": "THEN",
    "else": "ELSE",
    "end" : "END",
    "for" : "FOR",
    "while": "WHILE",
    "to"  : "TO",
    "next": "NEXT",
    "print": "PRINT",
    "var" : "VAR",
    "ptr" : "PTR",
    'def' : 'DEF',
    'do'  : 'DO',
    ','   : 'SEPARATOR',
    '&'   : 'ADDRESS',
    '"'   : 'QUOTE'
}

tokens = [
    'VARIABLE', 'NUMBER', 'STRING',
    'PLUS','MINUS','TIMES','DIVIDE', 'EQUALS', 'EXPONENT', 'REMAINDER',
    'LPAREN','RPAREN', 'LSQUARE', 'RSQUARE',
    'SEMICOLON',
    'INFERIOR', 'INFERIOR_OR_EQUAL', 'SUPERIOR', 'SUPERIOR_OR_EQUAL', 'DOUBLE_EQUALS', 'DIFFERENT'
] + list(reserved.values())

# Tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EXPONENT  = r'\*\*'
t_REMAINDER = r'%'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LSQUARE   = r'\['
t_RSQUARE   = r'\]'
t_VARIABLE  = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQUALS    = r'='
t_SEMICOLON = r';'
t_INFERIOR  = r'<'
t_INFERIOR_OR_EQUAL = r'<='
t_SUPERIOR  = r'>'
t_SUPERIOR_OR_EQUAL = r'>='
t_DOUBLE_EQUALS = r'=='
t_DIFFERENT = r'!='

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]+"'
    t.value = t.value[1:-1]
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_IF(t):
    r'if'
    return t

def t_THEN(t):
    r'then'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_END(t):
    r'end'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_TO(t):
    r'to'
    return t

def t_NEXT(t):
    r'next'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_VAR(t):
    r'var'
    return t

def t_PTR(t):
    r'ptr'
    return t

def t_DEF(t):
    r'def'
    return t

def t_DO(t):
    r'do'
    return t

def t_SEPARATOR(t):
    r','
    return t

def t_ADDRESS(t):
    r'&'
    return t

def t_QUOTE(t):
    r'"'
    return t

# Build the lexer
import ply.lex as lex
lex.lex()

# Precedence rules for the arithmetic operators
# moins prioritaire ---> plus prioritaire
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'REMAINDER'),
    ('right', 'UMINUS'),
    ('left', 'EXPONENT')
)

def p_scope(p):
    'scope : block'
    print(p[1])
    
    r = runtime(p[1])
    if r is not None:
        print(r);

def p_block(p):
    '''block : block statement
             | statement'''    
    if len(p) is 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[1])

def p_statement_condition(p):
    '''statement : IF LPAREN comparison RPAREN THEN block END
                 | IF LPAREN comparison RPAREN THEN block ELSE block END'''    
    if len(p) is 10:
        p[0] = ('IFELSE', p[3], p[6], p[8])
    else:
        p[0] = ('IF', p[3], p[6])

def p_statement_for(p):
    '''statement : FOR LPAREN NUMBER TO NUMBER RPAREN NEXT block END
                 | FOR LPAREN NUMBER TO VARIABLE RPAREN NEXT block END
                 | FOR LPAREN VARIABLE TO NUMBER RPAREN NEXT block END
                 | FOR LPAREN VARIABLE TO VARIABLE RPAREN NEXT block END'''
    a = p[3]
    b = p[5]

    if type(a) is str:
        a = ('RETURN', a)

    if type(b) is str:
        b = ('RETURN', b)
    
    p[0] = ('FOR', a, b, p[8])

def p_statement_while(p):
    'statement : WHILE LPAREN comparison RPAREN NEXT block END'    
    p[0] = ('WHILE', p[3], p[6])

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN SEMICOLON'        
    p[0] = ('PRINT', p[3])

def p_statement_assign(p):
    'statement : VARIABLE EQUALS expression SEMICOLON'
    p[0] = ('=', 'simple', p[1], p[3])

def p_statement_assign_pointer(p):
    'statement : ADDRESS VARIABLE EQUALS expression SEMICOLON'
    p[0] = ('=', 'pointer', p[2], p[4])

def p_statement_define(p):
    'statement : VAR VARIABLE EQUALS expression SEMICOLON'
    p[0] = ('DEFINE', 'simple', p[2], p[4])

def p_statement_define_pointer(p):
    'statement : PTR VARIABLE EQUALS VARIABLE SEMICOLON'
    p[0] = ('DEFINE', 'pointer', p[2], p[4])

def p_statement_define_function(p):
    'statement : DEF VARIABLE LPAREN RPAREN DO block END'    
    # p[0] = ('DEFINE', 'function', p[2], p[4], p[7])
    p[0] = ('DEFINE', 'function', p[2], None, p[6])

def p_statement_call_function(p):
    'statement : VARIABLE LPAREN RPAREN SEMICOLON'    
    p[0] = ('CALL_FUNCTION', p[1])

# fix bugs
def p_statement_arguments(p):
    '''arguments : argument SEPARATOR argument
                 | argument'''
    for item in enumerate(p):
        print('arguments', item)
        
    if len(p) is 4:
        p[0] = (p[1], p[3])
    else:
        p[0] = (p[1])

def p_statement_argument(p):
    '''argument : VARIABLE EQUALS expression
                | VARIABLE'''
    if len(p) is 4:
        p[0] = ('DEFAULT', p[1], p[3])
    else:
        p[0] = (p[1])
# fix bugs

def p_statement_expr(p):
    'statement : expression SEMICOLON'
    p[0] = p[1]

def p_comparison_binop(p):
    '''comparison : expression INFERIOR expression
                  | expression INFERIOR_OR_EQUAL expression
                  | expression SUPERIOR expression
                  | expression SUPERIOR_OR_EQUAL expression
                  | expression DOUBLE_EQUALS expression
                  | expression DIFFERENT expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EXPONENT expression
                  | expression REMAINDER expression
                  | expression INFERIOR expression
                  | expression INFERIOR_OR_EQUAL expression
                  | expression SUPERIOR expression
                  | expression SUPERIOR_OR_EQUAL expression
                  | expression DOUBLE_EQUALS expression
                  | expression DIFFERENT expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_select(p):
    'expression : VARIABLE LSQUARE expression RSQUARE'
    p[0] = ('AT', p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = ('RETURN', p[1])
    
    # try:
        # p[0] = variables[p[1]]
    # except LookupError:
        # print("Undefined variable '%s'" % p[1])
        # p[0] = 0

def p_error(p):
    raise PlySyntaxError(p.value)

import ply.yacc as yacc
yacc.yacc()

while True:
    try:
        s = input('calc > ')   # use input() on Python 3
    except EOFError:
        break

    try:
        yacc.parse(s)
    except PlyError as e:
        print(e)
    except Exception as e:
        e = PlyInternalError(e.__str__())
        print(e)
