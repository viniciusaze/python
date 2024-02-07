num = []
numpar = []
numimpar =[]
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    else:
        while continuar != 'S':
            continuar = input('Quer continuar? [S/N] ').strip().upper()
print('-=' * 20)
print(f'Lista: {num}')

for i, v in enumerate(num): #para checar os valores e separar par de impar
    if v % 2 == 0:
        numpar.append(v)
    else:
        numimpar.append(v)
print('-=' * 30)
print(f'Lista de números PARES: {numpar}')
print(f'Lista de números ÍMPARES: {numimpar}')