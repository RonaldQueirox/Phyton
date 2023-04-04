# Desafio 053

frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
jun = ''.join(pal)
inv = ''
inv = jun[::-1]
print('O inverso de {} é {}'.format(jun, inv))
if inv == jun:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')