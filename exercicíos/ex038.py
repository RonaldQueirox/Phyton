# Desafio 051

pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
décimo = pri + (10 - 1) * raz
for c in range(pri, décimo + raz, raz):
    print('{}'.format(c), end='-> ')
print('ACABOU')