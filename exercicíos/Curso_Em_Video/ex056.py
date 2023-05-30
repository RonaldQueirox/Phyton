# Desafio 069

tot18 = 0
while True:
    idade = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]' )).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')