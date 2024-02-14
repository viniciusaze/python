def fatorial(f):
    f = 1
    for c in range(num, 0 , -1):
        f *= num
        print(f'{f} x {num}')
    return f


num = int(input('Digite o número para cálculo do fatorial: '))
print(fatorial(num))