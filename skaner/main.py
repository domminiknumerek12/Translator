from scanner import Scanner
from tokens import *

with open("input.txt", "r", encoding="utf-8") as f:
    code = f.read()

scanner = Scanner(code)
html = "<html><body><pre>"

while True:
    token_type, token_value = scanner.get_token()
    
    if token_type == EOF:
        break
    
    color = COLORS.get(token_type, "#000000")
    safe_value = token_value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    if token_type == NEWLINE:
        html += "\n"
    elif token_type == WHITESPACE:
        html += safe_value
    elif token_type == STRING:
        html += f'<span style="color:{color};">&quot;{safe_value}&quot;</span>'
    else:
        html += f'<span style="color:{color};">{safe_value}</span>'

html += "</pre></body></html>"

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done")
