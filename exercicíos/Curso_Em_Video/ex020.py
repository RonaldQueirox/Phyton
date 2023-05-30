# Desafio 028

from random import randint
comp = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 10)
jog = int(input('Em Que Número Eu Pense ?: '))
if jog == comp:
    print('Você Acertou Parabéns !!!!')
else:
    print('Infelizmente Você Errou')

# Desafio 029

vel = int(input('Qual É a Velocidade Atual Do Seu Carro?: '))
if vel > 80:
    print('Você foi Multado !!!!, Foi Excedido A Velocidade Permitida')
    mul = (vel-80) * 7
    print('Terá Que Pagar Uma Multa De {} Estará Sendo Debitada Da Sua Conta'.format(mul))
else:
    print('Parabéns !!!!, Você Está Dentro Do Limite')



