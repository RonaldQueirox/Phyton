def aumentar(n):
    for c in n:
        c += 1
    return c + 1 if format is False else moeda(n)

def diminuir(n):
    for f in n:
        f -= 1
    return f - 1

def dobrar(n):
    return n * 2

def metade(n):
    res = n / 2
    return res

def moeda(n):
    return f'{moeda}{n}'.replace('.', '.')