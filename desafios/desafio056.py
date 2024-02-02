somaidade = 0
mih = 0 # Maior Idade Homem
nomevelho = ''
contm = 0
for p in range(1, 5):
    print(f'----- 1ª{p} -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        mih = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > mih:
        mih = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contm += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O nome do homem mais velho do grupo é {nomevelho}')
print(f'Ao total, {contm} mulheres tem menos de 20 anos.')