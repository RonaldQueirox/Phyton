# Desafio 066
print('-=-'*20)
soma = cont = 0
while True:
    num = int(input('Digite um val9r (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')