import ply.lex as lex
import sys

# reservadas = {
#     'uma' : 'main', 
#     'hun' : 'int', 
#     # 'chunka' : 'float',
#     'chillu' : 'bool', 
#     # 'chaqwa' : 'string',
#     'chaya' : 'return', 
#     'unan' : 'function', 
#     'ari' : 'if', 
#     'shuc' : 'else', 
#     'pacha' : 'while', 
#     'haykaq' : 'for' 
# }

reservadas = {
    'uma' : 'uma', #     'UMA', ##MAIN
    'hun' : 'hun', #     'HUNTA', ##int
    'chunka' : 'chunka', #      'CHUNKA', ##FLOAT
    'chillu' : 'chillu', #     'CHILLU', ##BOOL
    'chaya' : 'chaya', #     'CHAYA', ##RETURN
    'unan' : 'unan', #     'UNAN', ##FUNCTION
    'ari' : 'ari', #     'ARI', ##if
    'shuc' : 'shuc', #     'SHUC' ##else
    'pacha' : 'pacha', #     'PACHA', ##while
    'haykaq' : 'haykaq' #     'HAYKAQ', ##for
}

tokens = [
    'num',
    'dec',
    'boolean',
    # 'text',
    'opemasmas',
    'opesuma',
    'opemenos',
    'opemult',
    'opediv',
    'opemod',
    'igualq',
    'noigualq', 
    'menorq', 
    'menoriguq', 
    'mayorq', 
    'mayoiguq', 
    'parenl',
    'parenr',
    'and',
    'or',
    'assign',
    'keyl',
    'keyr',
    'id',
    'comma',
    'dotcomma',
] + list(reservadas.values())

#tokens = tokens+reservadas

t_ignore     = " \t" 
t_opemasmas  = r'\+\+'
t_opesuma    = r'\+'
t_opemenos   = r'\-'
t_opemult    = r'\*'
t_opediv     = r'/'
t_opemod     = r'%'
t_and        = r'&'
t_or         = r'\|'
t_assign     = r'='
t_igualq     = r'=='
t_noigualq   = r'<>'
t_menorq     = r'<'
t_menoriguq   = r'<='
t_mayorq     = r'>'
t_mayoiguq   = r'>='
t_parenl     = r'\('
t_parenr     = r'\)'
t_keyl       = r'\{'
t_keyr       = r'\}'
t_comma      = r'\,'
t_dotcomma   = r'\;'


def t_num(t):
    r'\d+'
    t.value = int(t.value) 
    return t

def t_dec(t):
    r'\d+'
    t.value = float(t.value) 
    return t

def t_boolean(t):
    r'true | false'
    return t

# def t_string(t):
#     r'"([^\\"]|\\")*")'    
#     t.type = reservadas.get(t.value,'text')    
#     return t

def t_id(t):
    r'[a-zA-Z]+ ( [a-zA-Z0-9]* )'    
    t.type = reservadas.get(t.value,'id')    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Character non valid '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def get_tokens(file):
    tokens = []
    f = open("EJEMPLOS/ejemplo_2.txt", "r")
    data = f.read()
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      
        #print(tok)
        #print(tok.type, tok.value, tok.lineno, tok.lexpos)
        #print( str(tok.type) + ' ', end='' )
        tokens.append( [tok.type, tok.value, tok.lineno] )

    return tokens

if __name__ == "__main__":
    tokens = get_tokens( sys.argv[0])
    for tok in tokens:
        print( str(tok[0]) + ' ', end='')
    print()

    print(tokens)