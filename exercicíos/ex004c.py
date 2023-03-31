# Desafio 011

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é um {}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de pinta'.format(tinta))

# Desafio 012

preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(preco, novo))

# Desafio 013

sal = float(input('Qual é o salário do Funcionário? R$'))
nov = sal + (sal * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a recebar R${:.2f}'.format(sal, nov))