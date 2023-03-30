
# a forma de faze-los ser somados a utilizando o termo int.

print('Digite suas notas para ter sua media !')
n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))
s = n1 + n2 + n3
media = s / 3 
print('Media das notas é: {}!'.format(media))

# este exemplo acima fica mais realista utlizando float, pois ira ter o ponto 
# veja o exemplo abaixo

print('Digite suas notas para ter sua media !')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
s = n1 + n2 + n3
media = s / 3 
print('Media das notas é: {}!'.format(media))
