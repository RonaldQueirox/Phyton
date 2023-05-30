# Desafio 059

n1 = int(input('Digite Um Valor: '))
n2 = int(input('Digite Outro Valor: '))
print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
''')

if n1 and n2 == 1:
    s = n1 + n2
    print('O Resultado Dos Valores é {}'.format(s))
elif n1 and n2 == 2:
    m = n1 * n2
    print('O Resultado Dos Valores é {}'.format(m))
elif n1 and n2 == 3:
    if n1 > n2:
        print('O {} é Maior Valor: '.format(n1))
    else:
        print('O {} é Maior Valor: '.format(n2))
    