print('-=-' * 20)
print('Números Ímpares')
print('-=-' * 20)
soma = 0
cont = 0
for c in range (0, 500, 3):
    if c % 3 == 0:
        soma = soma + 3
    cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))