from tokens import *

class Scanner:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.ch = self.next_char() if self.pos < len(text) else None
    
    def next_char(self):
        if self.pos < len(self.text):
            c = self.text[self.pos]
            self.pos += 1
            return c
        return None
    
    def current_char(self):
        if self.pos > 0:
            return self.text[self.pos - 1]
        return None
    
    def get_token(self):
        if self.ch is None:
            return (EOF, "")
        
        if self.ch == '\n':
            token = self.ch
            self.ch = self.next_char()
            return (NEWLINE, token)
        
        if self.ch == ' ' or self.ch == '\t':
            token = ""
            while self.ch and self.ch in ' \t':
                token += self.ch
                self.ch = self.next_char()
            return (WHITESPACE, token)
        
        if self.ch == '#':
            while self.ch and self.ch != '\n':
                self.ch = self.next_char()
            if self.ch == '\n':
                self.ch = self.next_char()
            return self.get_token()
        
        if self.ch in '"\'':
            quote = self.ch
            token = ""
            self.ch = self.next_char()
            while self.ch and self.ch != quote:
                token += self.ch
                self.ch = self.next_char()
            if self.ch == quote:
                self.ch = self.next_char()
            return (STRING, token)
        
        if self.ch.isdigit():
            token = ""
            while self.ch and self.ch.isdigit():
                token += self.ch
                self.ch = self.next_char()
            return (NUMBER, token)
        
        if self.ch.isalpha() or self.ch == '_':
            token = ""
            while self.ch and (self.ch.isalnum() or self.ch == '_'):
                token += self.ch
                self.ch = self.next_char()
            if token in KEYWORDS:
                return ("KEYWORD", token)
            return (IDENT, token)
        
        if self.ch in '+-*/%=<>!':
            token = self.ch
            self.ch = self.next_char()
            return (OPERATOR, token)
        
        if self.ch in '()[]{},:;.':
            token = self.ch
            self.ch = self.next_char()
            return (token, token)
        
        self.ch = self.next_char()
        return ("UNKNOWN", token)
