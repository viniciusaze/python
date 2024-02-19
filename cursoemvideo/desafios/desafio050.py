s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    cont = cont +1
    if n % 2 == 0:
        s += n
print(f'Você informou {cont} números, e a soma entre os PARES foi {s}')
