# Desafio 058

from random import randint
comp = randint(0, 10) # Faz o computador "PENSAR"
acertou = False
palpites = 0 
while not acertou:
    jog = int(input('Qual é seu palpite? '))
    palpites += 1
    if jog == comp:
        acertou = True
    else:
        if jog < comp:
            print('Mais... Tente mais uma vez.')
        elif jog > comp:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
