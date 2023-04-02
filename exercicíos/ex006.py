# Desafio 022

nm = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome.....')
print('Seu nome em maiúsculas é {}'.format(nm.upper))
print('Seu nome em minúsculas é {}'.format(nm.lower))
print('Seu nome tem ao todo {} letras'.format(len(nm) - nm.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nm.find(' ')))

# Desafio 023

num = int(input('Digite um número: ')).strip
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# Desafio 024

cid = str(input('Em que cidade você nasceu? ')).strip
print(cid[:5].upper() == 'SANTO')

# Desafio 025

nome = str(input('Qual é seu nome completp? ')).strip
print('Seu nome tem Silva {}'.format('silva' in nome.lower()))