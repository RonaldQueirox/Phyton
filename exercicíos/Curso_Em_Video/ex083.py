def soma(j, k):
    print(f'J = {j} e K = {k}')
    s = j + k
    print(f'A soma de J + K = {s}')
def soma3(l, d, g):
    print(f'L = {l} D = {d} e G = {g}')
    s = l + d + g
    print(f'A soma de L, D e G = {s}')
def lin():
    print('-=' * 30)
def contador(* núm): 
    # se usa o asterisco para diversos elemntos
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')


# Programa Principal
lin()
soma(8, 8)
soma(10, 12)
soma(4, 5)
print(soma)
lin()
# Somar três números

soma3(9, 7, 5)
soma3(12, 41, 21)
soma3(92, 29, 14)
print(soma3)
lin()

contador(9, 6, 5, 4, 3)
contador(4, 5, 6, 2, 1)
contador(5, 2, 1, 6, 8)