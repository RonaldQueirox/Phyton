# Desafio 081

valores = []
while True:
    valores.append(int('Digite um valor: '))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True) # Reveter a ordem dos números
print(f'Os valores em ordem decresencente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')