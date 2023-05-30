# Desafio 057

print('-=-' * 20)
sx = str(input('Escolha Entre: [M/F]')).strip().upper()[0]
while sx not in 'MmFf':
    sx = str(input('Dados Ínvalidos, Digite Novamente: '))
print('Sexo {} registrado com sucesso'.format(sx))
print('-=-' * 20)
