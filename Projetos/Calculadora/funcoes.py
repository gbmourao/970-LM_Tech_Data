def soma (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os inputs de 'a' e 'b' devem ser numéricos.")
    return a + b

def subtracao (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os inputs de 'a' e 'b' devem ser numéricos.")
    return a - b

def divisao (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os inputs de 'a' e 'b' devem ser numéricos.")
    elif b == 0:
        return("Erro: divisão por zero")
    return a/b

def multiplicacao (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os inputs de 'a' e 'b' devem ser numéricos.")
    return a*b