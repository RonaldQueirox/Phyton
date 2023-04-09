# Desafio 068
from random import randint 
v = 0
while True:
    jog = int(input('Diga um valor: '))
    comp = randint(0, 10)
    tol = jog + comp
    tip = ' '
    while tip not in 'PI':
        tip = str(input('Par ou Ímpar [P/I]')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador {comp}. Total de {tol}')
    print('DEU PAR' if tol % 2 == 0 else 'DEU ÍMPAR')
    if tip == 'P':
        if tol % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tip == 'I':
        if tol % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente....')