ficha = []

# CADASTRANDO ALUNOS, NOTAS E MÉDIA

while True:
    nome = input('Nome: ').upper().strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = input('Quer continuar? [S/N] ').upper().strip()
    if r == 'N':
        break
    else:
        while r != 'S':
            r = input('Quer continuar? [S/N] ').upper().strip()
print('-=' * 30)

# MOSTRANDO NA TELA

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}') # a[0] = NOME a[2] = MÉDIA
print('-' * 26)

# SELECIONANDO ALUNOS PARA MOSTRAR AS NOTAS

while True:
    print('-' * 35)
    opc = int(input('Quer mostrar as notas de qual aluno? (999 para cancelar) '))
    if opc == 999:
        print('FINALIZANDO.')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    elif opc > len(ficha) - 1:
        print('Aluno não encontrado.')
print('<<<< VOLTE SEMPRE >>>>')