# Desafio 044

print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
print('-=-' * 20)
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais No Cartão''')
print('-=-' * 20)
opc = int(input('Qual é a Opção? '))
if opc == 1:
    total = preco - (preco * 10 / 100)
elif opc == 2:
    total = preco - (preco * 5 / 100)
elif opc == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opc == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas Parcelas? '))
    parcela = total / totparc
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(preco, total))
