# Desafio 005

n1 = int(input('Digite um número: '))
ant = n1 - 1
suc = n1 + 1
print('o número {} é seu antecessor'.format(ant), end=' >>>> ')
print('o número {} é seu sucessor'.format(suc))

# Desaafio 006

n1 = int(input('Digite um número: '))
dob = n1 * 2
tri = n1 * 3
raz = n1 ** 1/2
print('o número {} é o dobro do número digitado'.format(dob), end=' >>>> ')
print('o número {} é o triplo do número digitado'.format(tri), end=' >>>> ')
print('o número {} é a raiz do número digitado'.format(raz))

# Desafio 007

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
s = n1 + n2 + n3
md = s / 3
print('Sua media é {:.1f}'.format(md))
