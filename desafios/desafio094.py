pessoa = {}
todos = []
cont = 0
media = 0
somaidade = 0
mulheres = []
acimamedia = []

while True:
    pessoa['nome'] = input('Nome: ').strip()
    sexo = input('Sexo: [M/F] ').strip().upper()

    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo: [M/F] ').strip().upper()
    if sexo == 'F':
        mulheres.append(pessoa['nome'])

    idade = int(input('Idade: ').strip())
    cont += 1    
    somaidade += idade
    media = somaidade / cont
    if idade > media:
        acimamedia.append(pessoa['nome'])

    pessoa['idade'] = idade
    pessoa['sexo'] = sexo
    todos.append(pessoa.copy())
    res = input('Quer continuar? [S/N] ').strip().upper()

    if res == 'N':
        
        break
    else:
        while res != 'S':
            res = input('Quer continuar? [S/N] ').strip().upper()

print('-=' * 30)
print(f'O grupo tem {cont} pessoas.')
print(f'A média de idade é de {media:.2f}')
print(f'As mulheres cadastradas são ', end='')
for m in mulheres:
    print(f'{m} ', end='')
print()
print(f'Lista de pessoas acima da média de idade: ', end='')
for i in acimamedia:
    print(f'{i} ', end='')
print()
print('<< ENCERRADO >>')