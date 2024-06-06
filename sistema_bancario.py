saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3


def Menu():
    opcao = input(''' Sistema Bancário
          
Selecione a opção desejada:
          
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
            
-->''').lower().strip()
    
    while True:

        if opcao == 'd':
            print('deposito')
            break
        elif opcao == 's':
            print('saque')
            break
        elif opcao == 'e':
            print('extrato')
            break
        elif opcao == 'q':
            break

Menu()