from random import randint
certo = randint(0, 5)
escolha = int(input('Escolha um número entre 0 e 5: '))
print('Será que você acertou?')
if certo == escolha:
    print(f'Parabéns!!! Acertou o número {certo}')
else:
    print(f'Que pena! Você errou... o número sorteado foi {certo}')
print('Fim do jogo')
