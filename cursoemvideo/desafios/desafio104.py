def leiaInt(n):
    while True:
        num = input(n)
        if num.isnumeric():
            return num
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
    
    

num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')