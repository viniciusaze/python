num = []
numpar = []
numimpar = []
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    if n % 2 == 0:
        numpar.append(n)
    else:
        numimpar.append(n)
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    else:
        while continuar != 'N' and continuar != 'S':
            continuar = input('Por favor, digite um valor válido. Quer continuar? [S/N] ').strip().upper()
print('-=' * 20)
print(f'Sua lista com todos os números: {num}')
print(f'Sua lista com números PARES: {numpar}')
print(f'Sua lista com números ÍMPARES: {numimpar}')