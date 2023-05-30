# Desafio 056

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1, 5):
    print('------{}ª PESSOA -------'.format(p))
    nome = str(input('nOME: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1:
        maioridadehomem = idade
        nomevelho = nome
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
