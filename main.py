import re


class Token:
    value = ''
    type = ''

    def __init__(self, _type, _value):
        self.value = _value
        self.type = _type


# label : regex
dictionary = {

    # Comments and other literals
    'SINGLE_COMMENT': r'(?m)//.*',  # (?m) . doesn't match \n
    'MULTI_COMMENT': r'(?s)/\*.*?\*/',  # (?s) . matches \n
    'STRING_LITERAL': r'(?m)".*?"',  # not greedy

    'INTEGER_LITERAL': r'\b\d\d*(?!\.)\b',  # (?!\.) not followed by .
    'FLOAT_LITERAL': r'\b\d\d*\.\d\d*',
    'CHAR_LITERAL': r"('.{0,1}?')",  # ''' is an error
    'EOF': r'\b0\b',

    # Data Types
    'INT': r'\bint\b',
    'BOOL': r'\bbool\b',
    'CHAR': r'\bchar\b',
    'DOUBLE': r'\bdouble',
    'FLOAT': r'\bfloat\b',
    'VOID': r'\bvoid\b',
    'CONST': r'\bconst\b',
    'AUTO': r'\bauto\b',
    'LONG': r'\blong\b',
    'SHORT': r'\bshort\b',
    'SIGNED': r'\bsigned\b',
    'UNSIGNED': r'\bunsigned\b',
    'STATIC': r'\bstatic\b',
    'VOLATILE': r'\bvolatile\b',

    # Data structures
    'STRUCT': r'\bstruct\b',
    'UNION': r'\bunion\b',

    # Reserved Words
    'RETURN': r'\breturn\b',
    'NEW': r'\bnew\b',
    'TRUE': r'\btrue\b',
    'FALSE': r'\bfalse\b',
    'SWITCH': r'\bswitch\b',
    'CASE': r'\bcase\b',
    'DEFAULT': r'\bdefault\b',
    'DO': r'\bdo\b',
    'WHILE': r'\bwhile\b',
    'FOR': r'\bfor\b',
    'BREAK': r'\bbreak\b',
    'CONTINUE': r'\bcontinue\b',
    'IF': r'\bif\b',
    'ELSE': r'\belse\b',
    'ENUM': r'\benum\b',
    'EXTERN': r'\bextern\b',
    'GOTO': r'\bgoto\b',
    'REGISTER': r'\bregister\b',
    'SIZEOF': r'\bsizeof\b',
    'TYPEDEF': r'\btybedef\b',

    # ALL Symbols

    'PLUS': r'\+(?!\+)',
    'MINUS': r'-(?!-)',
    'INCREMENT': r'\+\+',
    'DECREMENT': r'--',

    'ASTERICK': r'\*',
    'DIVIDE': r'\/',
    'MOD': r'%',

    'BITWISE_AND': r'&(?!&)',
    'AND': r'&&',
    'OR': r'\|\|',
    'BITWISE_OR': r'\|(?!\|)',
    'BITWISE_XOR': r'\^',
    'BITWISE_NOT': r'~',

    'LEFT_ROUND_B': r'\(',
    'RIGHT_ROUND_B': r'\)',
    'LEFT_CURLY_B': r'\{',
    'RIGHT_CURLY_B': r'\}',
    'LEFT_SQUARE_B': r'\[',
    'RIGHT_SQUARE_B': r'\]',

    'DOT': r'\.',
    'SEMICOLON': r';',
    'COMMA': r',',

    'PREPROCESSOR': r'#',
    'BACKWARD_SLASH': r'\\',

    'ASSIGN_OPERATOR': r'=(?!=)',
    'EQUAL': r'==',
    'NOT': r'\!(?!=)',
    'NOT_EQUAL': r'\!=',
    'LEFT_SHIFT': r'>>',
    'RIGHT_SHIFT': r'<<',
    'LESS_EQ': r'>=',
    'GREAT_EQ': r'<=',
    'LESSTHAN': r'>(?!>|=)',
    'GREATERTHAN': r'<(?!=|<)',

    # Identifier
    'ID': r'\b[_a-zA-Z][_a-zA-Z0-9]{0,30}\b',

}

# read the program from a file
f = open("code_to_tokenize.txt", 'r')
code = f.read()

tokens = []
while len(code) > 0:

    code = code.strip()
    m = None  # matched

    for l, r in dictionary.items():
        # label: regex
        m = re.match(r, code)
        if m:
            tokens.append(Token(l, m.group()))
            end = m.span()[1]
            code = code[end:]
            break

    if m is None:  # no matched regex
        print('error occurred while tokenizing the code at:\n', code)

# write on file
f = open("tokens.txt", "w")
for t in tokens:
    f.write(" < %s > %s \n" % (t.type, t.value))
f.close()

# thanks to regex101
