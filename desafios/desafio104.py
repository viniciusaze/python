def leiaInt(n):
    while True:
        num = input(n)
        if num not in '1234567890':
            print('ERRO! Digite um número inteiro válido!')
        else:
            return num
    
    

num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')