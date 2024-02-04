n = 0
soma = 0
c = 0
while n != 999:
    n = int(input('Digite um número: '))
    soma = soma + n
    c += 1
    print('Digite 999 para parar.')
print(f'Ao total você digitou {c - 1} números. E a soma deles foi de: {soma - 999}')