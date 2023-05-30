# Desafio 079

números = list() # criar lista
while True: # utiliza-se while True para criar "Looping Infinito"
    n = int(input('Digite um valor: '))
    if n not in números: # not in significa não esta
        números.append(n) # append serve para adiconar um valor a lista
        print('Valor adicionado com sucesso....')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break # usa break pra parar imediatamente o programa
print('-=' * 30)
print(f'Você digitou os valores {números}')

