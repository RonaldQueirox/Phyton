# Desafio 072
from time import sleep
print('-=-'*30)
numext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20'))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print('-=-'*30)
