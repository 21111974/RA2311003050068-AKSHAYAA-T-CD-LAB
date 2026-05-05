keywords = {"int", "float", "if", "else", "while"}

code = input("Enter code: ").split()

for word in code:
    if word in keywords:
        print(word, "-> Keyword")
    elif word.isidentifier():
        print(word, "-> Identifier")
    elif word.isdigit():
        print(word, "-> Constant")
    else:
        print(word, "-> Operator")
