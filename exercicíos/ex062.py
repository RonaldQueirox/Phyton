# Desafio 075

num = int(input('Digite Um Valor: ')),
int(input('Digite Um Segundo: '))
int(input('Digite Um Terceiro Valor: '))
int(input('Digite Um Quarto Valor: '))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

