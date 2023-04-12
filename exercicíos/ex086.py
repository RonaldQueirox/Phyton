# Desafio 096
def área(larg, alt):
    a = larg * alt
    print(f'A área de um terreno {larg}x{alt} é de {a}m².')


# Programa principal
print(' Controle de Terrenos')
print('-=' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)