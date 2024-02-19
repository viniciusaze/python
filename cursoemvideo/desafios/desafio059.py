n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0
while op != 5:
    op = int(input('''
====================
Escolha uma opção:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa
=====================
Opção: '''))

    if op == 1:
        print(f'SUA RESPOSTA:\n{n1} + {n2} = {n1+n2}')
    elif op == 2:
        print(f'SUA RESPOSTA\n{n1} x {n2} = {n1*n2}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior do que {n2}!')
        elif n2 > n1:
            print(f'{n2} é maior do que {n1}!')
        else:
            print(f'Os dois valores são iguais.')
    elif op == 4:
        n1 = int(input('Digite os novos valores do primeiro número: '))
        n2 = int(input('Digite os novos valores do segundo número: '))
    elif op > 5 or op < 1:
        print('Opção inválida. Tente novamente')
print('Fim do programa!')