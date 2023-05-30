n1 = float(input('Digite sua Primeira Nota: '))
n2 = float(input('Digite sua Segunda Nota: '))
n3 = float(input('Digite sua Terceira Nota:'))
s = n1 + n2 + n3
med = s / 3
if med >= 6:
    print('Parabéns Você Passou !!!!!')
else:
    print('Infelizmente Você Não Passou, Continue Estudando !!!')
