from time import sleep
import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo':True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo':False}]

def main():
    os.system('cls')
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
    print('3 - Alternar estado do Restaurante')
    print('4 - Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def exibir_subtitulo(texto):
    os.system('cls')
    print('*' * (len(texto) + 4))
    print(f'  {texto}')
    print('*' * (len(texto) + 4))

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    c = 1
    print(f'Nº| {'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(15)} | Status')
    for item in restaurantes:
        nome_restaurante = item['nome']
        categoria = item['categoria']
        ativo = 'Ativado' if item['ativo'] else 'Desativado'
        # Conceito ternário , passa o verdadeiro primeiro
        print(f'{c} - {nome_restaurante.ljust(25)} | {categoria.ljust(15)} | {ativo}')
        c += 1
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] 
            #not inverte o valor, de false para true ou vice versa.

            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            # Conceito ternário , passa o verdadeiro primeiro
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Finalizando o App...')
    sleep(2)
    exibir_subtitulo('APP FINALIZADO! Volte sempre!')
    sleep(3)
    os.system('cls') # Comando usado para limpar o terminal

if __name__ == '__main__':
    main()