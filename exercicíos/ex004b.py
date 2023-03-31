# Desafio 008

m = int(input('Digite uma metragem: '))
cm = m * 100
mm = m * 1000
print('o numero que voce digitou dá {}cm em centímetros'.format(cm), end=' >>>> ')
print('o numero que voce digitou dá {}mm em milímetros'.format(mm))

# Desafio 009
t = int(input('Digite um algarismo: '))
t1 = t * 1
t2 = t * 2
t3 = t * 3
t4 = t * 4
t5 = t * 5
t6 = t * 6
t7 = t * 7
t8 = t * 8
t9 = t * 9
print('Esta é a tabuada do número digitado >>>>> {} {} {} {} {} {} {} {} {} '.format(t1, t2, t3, t4, t5, t6, t7, t8, t9))

# Desafio 010

din = float(input('Quanto você tem na carteira? :'))
dol = din / 3.27
print('Você tem {:.1f} doláres'.format(dol))