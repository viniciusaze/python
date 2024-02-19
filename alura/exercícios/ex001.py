#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'Número {n} é PAR!')
else:
    print(f'Número {n} é ÍMPAR!')