x = input('Digite algo: ')

print('Qual o tipo primitivo desse objeto?',type(x))

print('O objeto digitado é um número?', x.isnumeric())

print('O objeto digitado são caracteres?',x.isalpha())

print('O objeto digitado contém números e/ou caracteres (Alfanumérico)?',x.isalnum())

print('O objeto digitado está em todo em letras maiúsculas?',x.isupper())

print('O objeto digitado está em todo em letras minúsculas?',x.islower())

print('O objeto digitado está capitalizado?', x.istitle())