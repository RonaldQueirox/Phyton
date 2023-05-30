print('-=-' * 20)
n1 = float(input('Digite sua Primeira Nota: '))
n2 = float(input('Digite sua Segunda Nota: '))
n3 = float(input('Digite sua Terceira Nota: '))
n4 = float(input('Digite sua Quarte Nota: '))
print('-=-' * 20)
s = n1 + n2 + n3 + n4
med = s / 4
print('Sua Média é {:.2f}'.format(med))
if med >= 6 and med <= 7.9:
    print('Você Passou Parabéns !!!')
elif med >= 8:
    print('Você Passou Com Louvor !!!!!')
else:
    print('Infelizmente Você Não Passou, Estude Mais !!!!')
