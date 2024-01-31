n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('Calculando a sua média...')
if media < 6:
    print(f'Média {media:.1f}, aluno REPROVADO!')
else:
    print(f'Média {media:.1f}, aluno APROVADO')
print('Boas férias!')