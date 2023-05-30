# Desafio 034

sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    nv = sal + (sal * 15 / 100)
else:
    nv = sal + (sal * 10 / 100)
print('Quem ganhava R${:.F} passa a ganhar R${:.2f} agora'.format(sal, nv))

# Desafio 035

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: