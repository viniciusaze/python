def ajuda(txt):
    while True:
        print('\033[0;30;41m~' * len(txt))
        print(txt)
        print('\033[0;30;41m~\033[m' * len(txt))
        fun = input('Função ou Biblioteca > ').strip().lower()
        if fun == 'fim':
            print('\033[0;30;42m>>> ATÉ LOGO <<<\033[m')
            break
        else:
            print('\033[0;30;44m~' * 45)
            print(f'  ACESSANDO O MANUAL DO COMANDO {fun}  ')
            print('\033[0;30;44m~\033[m' * 45)
            help(fun)


ajuda('\033[0;30;41m  SISTEMA DE AJUDA PyHELP  ')