# Lexical Analyzer Program

keywords = {"int", "float", "if", "else", "while", "return"}

operators = {"+", "-", "*", "/", "=", "==", "<", ">", "<=", ">="}
delimiters = {"(", ")", "{", "}", ";", ","}

code = input("Enter source code: ").split()

for word in code:
    if word in keywords:
        print(word, "-> Keyword")
    elif word in operators:
        print(word, "-> Operator")
    elif word in delimiters:
        print(word, "-> Delimiter")
    elif word.isdigit():
        print(word, "-> Constant")
    elif word.isidentifier():
        print(word, "-> Identifier")
    else:
        print(word, "-> Unknown")
