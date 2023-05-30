# Desafio 036

casa = int(input('Qual é o Valor da Casa: '))
sal= int(input('Qual é seu Salário: '))
anos = int(input('Em Quantos Anos Você Vai Pagar: '))
pres = casa / (anos * 12)
min = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('a prestação será de R${:.2F}'.format(pres))
if pres <= min:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')