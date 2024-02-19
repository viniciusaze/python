aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
aluno['situação'] = 'Aprovado', 'Reprovado', 'Recuperação'
print('-=' * 25)
print(f'Nome é igual a {aluno['nome']}.')
print(f'A média de {aluno['nome']} é igual a {aluno['media']}.')
if aluno['media'] >= 6 and aluno['media'] < 7:
    print(f'Situação: {aluno['situação'][2]}')
elif aluno['media'] >= 7:
    print(f'{aluno['nome']}: {aluno['situação'][0]}')
else:
    print(f'Situação: {aluno['situação'][1]}')