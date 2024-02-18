def linha(tam=42):
    return '-' * 42

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite uma opção válida\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mERRO: O usúrario não informou a opção\033[m')
            return 0
        else:
            return n

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc