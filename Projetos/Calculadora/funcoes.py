def soma (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Os números digitados devem ser int ou float")
    return a + b