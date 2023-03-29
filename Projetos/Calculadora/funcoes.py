def soma (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Os números digitados devem ser int ou float")
    return a + b

def subtracao (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Os númegros digitados devem ser int ou float")
    return a - b

def divisao (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Os númegros digitados devem ser int ou float")
    elif b == 0:
        print("Erro: divisão por zero")
    return a/b