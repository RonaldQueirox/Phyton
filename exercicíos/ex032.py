from random import randint 
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(.5) # Para Espera Um Segundo
print('KEN')
sleep(.5)
print('PO!!!!!')
sleep(.5)
print('-=-' * 20)
sleep(.3)
print('Computador jogou {}'.format(itens[comp]))
sleep(.3)
print('Jogador jogou {}'.format(itens[jogador]))
sleep(.3)
print('-=-' * 20)
if comp == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
if comp == 1: # computador jogou PAPEL
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
if comp == 2: # computador jogou TESOURA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE') 
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')