n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('Calculando os valores')

if n1 > n2:
    print(f'O PRIMEIRO valor \033[1;42m{n1}\033[m é MAIOR!')
elif n1 < n2:
    print(f'O SEGUNDO valor \033[1;42m{n2}\033[m é MAIOR!')
else:
    print(f'Os dois valores \033[1;44m{n1} e {n2}\033[m são IGUAIS!')