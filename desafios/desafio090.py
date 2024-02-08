aluno ={}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
aluno['situação'] = 'Aprovado', 'Reprovado'
print(f'Nome é igual a {aluno['nome']}.')
print(f'A média de {aluno['nome']} é igual a {aluno['media']}.')
if aluno['media'] < 6:
    print(f'Situação: {aluno['situação'][1]}')
else:
    print(f'Situação: {aluno['situação'][0]}')