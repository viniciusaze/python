from time import sleep
import os
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def exibir_nome_do_programa():
    print("""
░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      """)

def exibir_opcoes():
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurante')
    print('3 - Ativar Restaurante')
    print('4 - Sair\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Cadastrar Restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            finalizar_app()
        case _: # Padrão coringa,corresponde a qualquer valor que não tenha sido correspondido pelos casos anteriores
            print('Opção inválida')

def finalizar_app():
    print('Finalizando o App...')
    sleep(2)
    print('APP FINALIZADO! Volte sempre!')
    sleep(3)
    os.system('cls') # Comando usado para limpar o terminal

if __name__ == '__main__':
    main()