a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))

# utiliza-se type para então mostrar o tipo primitivo da variavel

print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('E alfanúmerico? ', a.isalnum())
print('Está em maiúsculas ', a.isupper())
print('Está em minúsculas', a.islower())
print('Está em capitalizada', a.istitle())

