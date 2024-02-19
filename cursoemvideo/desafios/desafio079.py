numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Número duplicado, não será adicionado')
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    while continuar != 'S' and continuar != 'N':
        continuar = input('Digite um valor válido. Quer continuar? [S/N] ').strip().upper()
    
print(f'Lista: {numeros}')
numeros.sort()
print(f'Os números em ordem crescente são: {numeros}')

