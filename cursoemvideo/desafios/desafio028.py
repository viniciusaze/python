from random import randint
from time import sleep
certo = randint(0, 5) # Randomiza o número
print('*~*~' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('*~*~' * 15)

escolha = int(input('Em que número eu pensei? ')) # Jogador escolhe o número

print('Será que você acertou?')
sleep(2) # Deixa um tempo de 2s para o proximo passo

if certo == escolha:
    print(f'Parabéns!!! Acertou o número {certo}')
else:
    print(f'Não foi dessa vez! O número certo era {certo}, você escolheu o {escolha}')
print('Fim do jogo')
