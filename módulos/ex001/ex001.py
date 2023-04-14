# Desafio 107
import moeda

p = float(input('Digite um número: '))
print(f'A metade de {p} é {moeda.metade}')
print(f'O dobro de {p} é {moeda.dobrar}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')