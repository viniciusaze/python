while True:
    try:
        n1 = int(input('Digite um número Inteiro: '))
    except KeyboardInterrupt:
        print('\n\033[0;31mO usuário preferiu não digitar o valor\033[m')
        n1 = 0
        break
    except:
        print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m')
    else:
        break
while True:
    try:
        n2 = float(input('Digite um número Real: '))
    except KeyboardInterrupt:
        print('\n\033[0;31mO usuário preferiu não digitar o valor\033[m')
        n2 = 0
        break
    except:
        print('\033[0;31mERRO: Por favor, digite um número real válido.\033[m')
    else:
        break
print(f'O valor inteiro digitado foi {n1} e o valor real digitado foi {n2}.')