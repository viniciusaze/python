n = 0
soma = 0
c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'A soma dos {c} valores foi: {soma}')