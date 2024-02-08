num = [[], []] #Decalarando duas listas internas
valores = 0
c = 1
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    c += 1
    if valor % 2 == 0:
        num[0].append(valor) #Para adicionar o valor na posição 0
    else:
        num[1].append(valor)
print('-=' * 20)
num[0].sort()
num[1].sort()
print(f'Valores: {num}')
print(f'Valores PARES: {num[0]}')
print(f'Valores ÍMPARES: {num[1]}')


