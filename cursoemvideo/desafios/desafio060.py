n = int(input('Digite um número: '))
c = n
f = 1 # 1 é o fator nulo de multiplicação
print(f'Calculando {n}!')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f = f * c
    c -= 1
print(f'{f}')