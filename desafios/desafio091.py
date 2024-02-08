from random import randint
from time import sleep
jogo = {}
lista = []
print('Valores sorteados:')
for c in range(1, 5):
    jogo['jogador'] = c
    jogo['dado'] = randint(1, 6)
    lista.append(jogo.copy())
    sleep(1)
    print(f'O Jogador {jogo['jogador']} tirou {jogo['dado']}')

print('Ranking dos jogadores:')
print(jogo)
    

