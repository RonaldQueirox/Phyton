# Desafio 078

listanum = [] # criar uma lista
mai = 0 # adicionar a variavel maior
men = 0 # adicionar a variavel menor
for c in range(0, 5):
    # listanum.append para adicionar um valor a lista
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c] # o maior e o menor são iguais pois ainda não foram digitados
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('-='*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='') # end e para não quebrar a linha
for i, v in enumerate(listanum): #enumerate serve para enumerar os números
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} mas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()

