valores = []

# Para adicionar valores a lista:

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, n in enumerate(valores): # Para mostrar a posição dos valores
    print(f'Na posição {c}, o valor é de {n}.')
print('Fim da lista')