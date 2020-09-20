import ply.lex as lex
import log 
class AsplaLexer(object): 
    tokens = [
       'NUMBER',
       'PLUS',
       'TIMES',
       'LPAREN',
       'RPAREN',
    ]

    t_PLUS    = r'\+'
    t_TIMES   = r'\*'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    def t_NUMBER(self, t):
        r'[\d.]+'
        t.value = t.value    
        return t

    # # Define a rule so we can track line numbers
    # def t_newline(self, t):
    #     r'\n+'
    #     t.lexer.lineno += len(t.value)

    # # Error handling rule
    # def t_error(self, t):
    #     log.error("Illegal character '%s'" % t.value[0])
    #     t.lexer.skip(1)

    def test(self, s):
        # input data in lexer
        self.lexer.input(s)
        # for token in self.lexer.token():
        #     print(token)
        token = self.lexer.token()
        while token:
            log.debug(token)
            token = self.lexer.token()

input = '(3 + 412.5) * 5'
aspla = AsplaLexer()
print(aspla.test(input))
# with open('./test/complex.aspla', 'r') as f:
#     aspla = AsplaLexer()
#     aspla.test(f.read())
