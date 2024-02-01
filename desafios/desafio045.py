from random import choice
from time import sleep

print('-*' * 25)
print('Vamos jogar, será que você me ganha ??? HEHEHEHEHE')
print('-*' * 25)

jogador = input('Escolha sua jogada: \nPEDRA \nPAPEL \nTESOURA ').strip().lower()
lista = ['PEDRA','PAPEL','TESOURA']
pc = choice(lista).lower()

print('Preparando a minha jogada...')
sleep(3)

#JOGADA TESOURA

if jogador == 'tesoura' and pc == 'papel':
    print(f'\033[1;30;42mPARABÉNS! Você me venceu.\nVocê escolheu {jogador.capitalize()} e eu Papel.\033[m')
elif jogador == 'tesoura' and pc == 'pedra':
    print(f'\033[1;30;41mPERDEU! Você escolheu {jogador.capitalize()} e eu Pedra!\033[m')
elif jogador == 'tesoura' and pc == 'tesoura':
    print(f'\033[1;30;44mEmpatamos, ambos escolhemos Tesoura!\033[m')

#JOGADA PEDRA
    
elif jogador == 'pedra' and pc == 'papel':
    print(f'\033[1;30;41mPERDEU! Você escolheu {jogador.capitalize()} e eu Papel!\033[m')
elif jogador == 'pedra' and pc == 'tesoura':
    print(f'\033[1;30;42mPARABÉNS! Você me venceu.\nVocê escolheu {jogador.capitalize()} e eu Tesoura.\033[m')
elif jogador == 'pedra' and pc == 'pedra':
    print(f'\033[1;30;44mEmpatamos, ambos escolhemos Pedra!\033[m')

#JOGADA PAPEL
    
elif jogador == 'papel' and pc == 'pedra':
    print(f'\033[1;30;42mPARABÉNS! Você me venceu.\nVocê escolheu {jogador.capitalize()} e eu Pedra.\033[m')
elif jogador == 'papel' and pc == 'tesoura':
    print(f'\033[1;30;41mPERDEU! Você escolheu {jogador.capitalize()} e eu Tesoura!\033[m')
elif jogador == 'papel' and pc == 'papel':
    print(f'\033[1;30;44mEmpatamos, ambos escolhemos Papel!\033[m')

else:
    print('\033[4;37;41m[ERRO] Digite uma jogada válida!!!\033[m')