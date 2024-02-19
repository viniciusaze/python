num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número entre 0 e 20: '))

while n > 20 or n < 0:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
if n <= 20 and n >= 0:
    print(f'Você digitou o número {num[n]}')
    continuar = input('Quer continuar? [S/N]').strip().upper()
    while continuar != 'N':
        continuar = input('Quer continuar? [S/N]').strip().upper()
        if continuar == 'S':
            n = int(input('Digite um número entre 0 e 20: '))
            print(f'Você digitou o número {num[n]}')
print('FIM DO PROGRAMA')