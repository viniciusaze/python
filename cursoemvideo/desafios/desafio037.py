n = int(input('Informe um número inteiro para conversão:'))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opção == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif opção == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('[ERRO] Digite um valor válido')