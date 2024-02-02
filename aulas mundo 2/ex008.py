n = 1
pares = 0
impares = 0
cont = 0
while n != 0:
    n = int(input('Digite um número: '))
    cont += 1
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f'Você digitou {cont} números.')
print(f'PARES: {pares}')
print(f'ÍMPARES: {impares}')