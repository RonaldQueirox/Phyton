# Desafio 014

c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))

# Desafio 015

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pag = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pag))