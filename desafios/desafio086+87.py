l = 0
c = 0
matriz =[]
dados1 = []
dados2 = []
dados3 = []
for c in range(0, 3):
    n = int(input(f'Digite um valor para [{l},{c}]: '))
    c += 1
    dados1.append(n)
    matriz.append(dados1[:])
    dados1.clear()
l = 1
c = 0
for c in range(0, 3):
    n = int(input(f'Digite um valor para [{l},{c}]: '))
    c += 1
    dados2.append(n)
    matriz.append(dados2[:])
    dados2.clear()
l = 2
c = 0
for c in range(0, 3):
    n = int(input(f'Digite um valor para [{l},{c}]: '))
    c += 1
    dados3.append(n)
    matriz.append(dados3[:])
    dados3.clear()

print('-=' * 20)
for n in matriz[:3]:
    print(f'{n}', end='')
print()
for n in matriz[3:6]:
    print(f'{n}', end='')
print()
for n in matriz[6:10]:
    print(f'{n}', end='')
print()
print('-=' * 20)

somapar = 0
for n in matriz:
    for num in n:
        if num % 2 == 0:
            somapar += num
print(f'A soma dos valores pares é de : {somapar}')

somacol = 0
for n in (matriz[2::3]):
    for num in n:
        somacol += num
print(f'A soma entre os valores da terceira coluna é de: {somacol}')

maior = 0
for n in (matriz[3:6]):
    for num in n:
        if num > maior:
            maior = num
print(f'O maior número da segunda linha é o: {maior}')
