# Desafio 030

pr = int(input('Digite Um Número: '))
res = pr % 2
if res == 0:
    print('O número {} é PAR'.format(pr))
else:
    print('O número {} é IMPAR'.format(pr))

# Desafio 031

dis = int(input('Distância de uma viagem: '))
if dis <= 200:
    prec = dis * 0.50
else:
    prec = dis * 0.45
print('É o preço da sua passagem será de R${:.f}'.format(prec))

# Desafio 032

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

# Desafio 033
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
