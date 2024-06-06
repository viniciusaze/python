from time import sleep
import os

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


def Menu():
    os.system('cls')

    opcao = input(''' Sistema Bancário
          
Selecione a opção desejada:
          
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
            
--> ''').lower().strip()
    
    while True:

        if opcao == 'd':
            Deposito()
        elif opcao == 's':
            Saque()
        elif opcao == 'e':
            Extrato()
        elif opcao == 'q':
            break


def Deposito():
    os.system('cls')

    global saldo, extrato

    deposito = float(input('''
DEPÓSITO
Valor a depositar: R$ '''))
    
    saldo += deposito

    extrato += f'Depósito - R$ {deposito}\n'

    Menu()

def Saque():
    os.system('cls')

    global saldo, limite, numero_saques, LIMITE_SAQUES, extrato   

    saque = float(input('''
SAQUE
Valor a sacar: R$ '''))
    
    while True:
        if saque > 500:
            os.system('cls')
            print('Seu saque excede o limite de 500.')
            sleep(5)
            Saque()
        else:
            break
    
    if saque > saldo:
        os.system('cls')
        print('Você não possui saldo suficiente para esta transação')
        sleep(5)
        Saque()
    
    numero_saques += 1

    if numero_saques > LIMITE_SAQUES:
        os.system('cls')
        print('Você atingiu o limite de saques')
        sleep(5)
        Menu()

    saldo -= saque

    extrato += f'Saque - R$ {saque}\n'

    Menu()
    
def Extrato():
    global extrato, saldo
    print(f'EXTRATO\n{extrato} Saldo Total: {saldo}')

    sair = input('Aperte uma tecla para sair ')
    Menu()
    

Menu()


