from inspect import currentframe
from exceptions.error import PlyError
from exceptions.internalerror import PlyInternalError
from exceptions.rangeerror import PlyRangeError
from exceptions.syntaxerror import PlySyntaxError
from exceptions.typeerror import PlyTypeError

from runtime import runtime, Variable

reserved = {
    'if'    : 'IF',
    'then'  : 'THEN',
    'else'  : 'ELSE',
    'end'   : 'END',
    'for'   : 'FOR',
    'while' : 'WHILE',
    'to'    : 'TO',
    'next'  : 'NEXT',
    'print' : 'PRINT',
    'var'   : 'VAR',
    'const' : 'CONST',
    'def'   : 'DEF',
    'do'    : 'DO',
    ','     : 'SEPARATOR',
    '&'     : 'ADDRESS',
    '"'     : 'QUOTE',
    'typeof': 'TYPEOF',
    'delete': 'DELETE'
}

tokens = [
    'VARIABLE', 'NUMBER', 'STRING',
    'PLUS','MINUS','TIMES','DIVIDE', 'EQUALS', 'EXPONENT', 'REMAINDER',
    'LPAREN','RPAREN', 'LSQUARE', 'RSQUARE',
    'SEMICOLON', 'COLON',
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
t_COLON     = r':'
t_INFERIOR  = r'<'
t_INFERIOR_OR_EQUAL = r'<='
t_SUPERIOR  = r'>'
t_SUPERIOR_OR_EQUAL = r'>='
t_DOUBLE_EQUALS = r'=='
t_DIFFERENT = r'!='

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    # t.value = int(t.value)
    t.value = float(t.value) if '.' in t.value else int(t.value)
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

def t_CONST(t):
    r'const'
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

def t_TYPEOF(t):
    r'typeof'
    return t

def t_DELETE(t):
    r'delete'
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
        print(r)

def p_block(p):
    '''block : block statement
             | statement'''
    l = len(p)
    if l is 2:
        p[0] = (p[1])
    elif l is 3:
        p[0] = (p[1], p[2])

def p_statement_condition(p):
    '''statement : IF LPAREN comparison RPAREN THEN block END
                 | IF LPAREN comparison RPAREN THEN block ELSE block END'''
    l = len(p)
    if l is 8:
        p[0] = ('IF', p[3], p[6])
    elif l is 10:
        p[0] = ('IFELSE', p[3], p[6], p[8])

def p_statement_for(p):
    '''statement : FOR LPAREN expression TO expression RPAREN NEXT block END'''
    p[0] = ('FOR', p[3], p[5], p[8])

def p_statement_while(p):
    'statement : WHILE LPAREN comparison RPAREN NEXT block END'    
    p[0] = ('WHILE', p[3], p[6])

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN SEMICOLON'        
    p[0] = ('PRINT', p[3])

def p_statement_assign(p):
    '''statement : VARIABLE EQUALS expression SEMICOLON
                 | VARIABLE EQUALS ADDRESS VARIABLE SEMICOLON'''
    l = len(p)
    if l is 5:
        p[0] = ('=', Variable.number | Variable.string | Variable.array, p[1], p[3])
    elif l is 6:
        p[0] = ('=', Variable.pointer | Variable.unknown, p[1], p[4])

def p_statement_assign_pointer(p):
    'statement : ADDRESS VARIABLE EQUALS expression SEMICOLON'
    p[0] = ('=', Variable.pointer | Variable.reference, p[2], p[4])

def p_statement_assign_element(p):
    '''statement : VARIABLE LSQUARE expression RSQUARE EQUALS expression SEMICOLON
                 | ADDRESS VARIABLE LSQUARE expression RSQUARE EQUALS expression SEMICOLON'''
    l = len(p)
    if l is 8:
        p[0] = ('SETAT', Variable.char | Variable.array, p[1], p[3], p[6])
    elif l is 9:
        p[0] = ('SETAT', Variable.pointer | Variable.reference | Variable.char | Variable.array, p[2], p[4], p[7])

def p_statement_define(p):
    '''statement : VAR VARIABLE EQUALS expression SEMICOLON
                 | VAR VARIABLE EQUALS ADDRESS VARIABLE SEMICOLON'''
    l = len(p)
    if l is 6:
        p[0] = ('DEFINE', Variable.number | Variable.string | Variable.array, True, p[2], p[4])
    elif l is 7:
        p[0] = ('DEFINE', Variable.pointer | Variable.unknown, True, p[2], p[5])

def p_statement_define_constant(p):
    '''statement : CONST VARIABLE EQUALS expression SEMICOLON
                 | CONST VARIABLE EQUALS ADDRESS VARIABLE SEMICOLON
                 | CONST VARIABLE EQUALS LSQUARE cargument RSQUARE SEMICOLON'''
    l = len(p)
    if l is 6:
        p[0] = ('DEFINE', Variable.number | Variable.string, False, p[2], p[4])
    elif l is 7:
        p[0] = ('DEFINE', Variable.pointer | Variable.unknown, False, p[2], p[5])
    elif l is 8:
        p[0] = ('DEFINE', Variable.array, False, p[2], p[5])

def p_statement_define_function(p):
    '''statement : DEF VARIABLE LPAREN dargument RPAREN DO block END
                 | DEF VARIABLE LPAREN RPAREN DO block END'''
    l = len(p)
    if l is 8:
        p[0] = ('DEFINE', Variable.function, False, p[2], None, p[6])
    elif l is 9:
        p[0] = ('DEFINE', Variable.function, False, p[2], p[4], p[7])

def p_statement_call_function(p):
    '''statement : VARIABLE LPAREN cargument RPAREN SEMICOLON
                 | VARIABLE LPAREN RPAREN SEMICOLON'''
    l = len(p)
    if l is 5:
        p[0] = ('CALL_FUNCTION', p[1], None)
    elif l is 6:
        p[0] = ('CALL_FUNCTION', p[1], p[3])

def p_statement_define_argument(p):
    '''dargument : dargument SEPARATOR VARIABLE
                 | VARIABLE'''
    l = len(p)
    if l is 2:
        p[0] = (p[1])
    elif l is 4:
        p[0] = (p[1], p[3])

def p_statement_call_argument(p):
    '''cargument : cargument SEPARATOR expression
                 | expression'''
    l = len(p)
    if l is 2:
        p[0] = tuple([p[1]])
    elif l is 4:
        if type(p[1]) is tuple:
            p[0] = tuple(list(p[1]) + [ p[3] ])
        else:
            p[0] = tuple([ p[1] ] + [ p[3] ])

def p_statement_delete(p):
    'statement : DELETE VARIABLE SEMICOLON'
    p[0] = ('DELETE', p[2])

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

def p_expression_typeof(p):
    'expression : TYPEOF LPAREN VARIABLE RPAREN'
    p[0] = ('TYPEOF', p[3])

def p_expression_select(p):
    'expression : VARIABLE LSQUARE expression RSQUARE'
    p[0] = ('GETAT', p[1], p[3])

def p_expression_substring(p):
    '''expression : VARIABLE LSQUARE expression COLON expression RSQUARE
                  | VARIABLE LSQUARE COLON expression RSQUARE
                  | VARIABLE LSQUARE expression COLON RSQUARE
                  | VARIABLE LSQUARE COLON RSQUARE'''
    l = len(p)
    if l is 5:
        p[0] = ('SUBSTRING', p[1], None, None)
    elif l is 6:
        if p[3] == ':':
            p[0] = ('SUBSTRING', p[1], None, p[4])
        else:
            p[0] = ('SUBSTRING', p[1], p[3], None)
    elif l is 7:
        p[0] = ('SUBSTRING', p[1], p[3], p[5])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_array(p):
    'expression : LSQUARE cargument RSQUARE'
    p[0] = (p[2])

def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = ('RETURN', p[1])

def p_error(p):
    raise PlySyntaxError(currentframe(), p.value)

import ply.yacc as yacc
yacc.yacc()

while True:
    try:
        s = input('>> ')
    except EOFError:
        break

    try:
        yacc.parse(s)
    except PlyError as e:
        print(e)
    except Exception as e:
        e = PlyInternalError(currentframe(), e.__str__())
        print(e)
