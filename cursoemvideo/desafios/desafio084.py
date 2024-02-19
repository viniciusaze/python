pessoas = []
dados = []
pcont = 0
maior = 0
menor = 0
while True:
    dados.append(input('Nome: ')) #dados[0]
    dados.append(float(input('Peso: '))) #dados[1]
    if len(pessoas) == 0:
        maior = menor = dados[1]
        pessoamaior = pessoamenor = dados[0]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    r = input('Quer continuar? [S/N] ').strip().upper()
    pcont += 1
    dados.clear()
    if r == 'N':
        break
    else:
        while r != 'S':
            r = input('Quer continuar? [S/N] ').strip().upper()
print(f'-=' * 30)
print(pessoas)
print(f'Pessoas cadastradas: {pcont} pessoas.') # Pode se usar o (len(pessoas) tambem)

print(f'O maior peso foi de {maior}Kg, do usuário(a)',end=' ')
for p in pessoas:
    if p[1] == maior: #Peso p[1] 
        print(f'{p[0]}', end=' ') # Pessoa p[0]
print()
print(f'O menor peso foi de {menor}Kg, do usuário(a)', end=' ')
for p in pessoas:
    if p[1] == menor: #Peso p[1] 
        print(f'{p[0]}', end=' ') # Pessoa p[0]