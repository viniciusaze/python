numeros = []
cont = 0
while True:
    numeros.append(int(input('Digite um número: ')))
    cont += 1
    continuar = input('Quer continuar? [S/N] ').upper().strip()
    if continuar == 'N':
        break
    else:
        while continuar != 'S':
            continuar = input('Quer continuar? [S/N] ').upper().strip()
print('-=' * 30)
print(f'Sua lista: {numeros}')
print(f'A quantidade de valores digitados foi: {cont}')
numeros.sort(reverse=True)
print(f'Lista em ordem decrescente: {numeros}')
if 5 in numeros:
    print('O valor 5 está na lista.')
else:
    print('O valor NÃO está na lista.')

