def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não definido para numeros negativos!")
    if not isinstance(n, int):
        raise TypeError("Fatorial só pe definido para númros não decimais!")
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    

