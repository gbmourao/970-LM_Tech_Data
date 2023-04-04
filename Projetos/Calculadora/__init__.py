import funcoes

def calcule():
    a = input("Digite o 1º número: ")
    b = input("Digite o 2º número: ")
    try:
        a = float(a)
        b = float(b)
    except:
        raise TypeError("Os inputs de 'a' e 'b' devem ser numéricos.")
    operacao = input("Qual operação deseja fazer? ")
    if operacao == 'soma' or operacao == '+':
        return funcoes.soma(a, b)
    if operacao == 'subtracao' or operacao == '-':
        return funcoes.subtracao(a, b)
    if operacao == 'divisao' or operacao == '/':
        return funcoes.divisao(a, b)
    if operacao == 'multiplicacao' or operacao == '*':
        return funcoes.multiplicacao(a, b)