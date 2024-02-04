from random import randint
print('~' * 25)
print('JOGO DA ADVINHAÇÃO 2.0')
print('~' * 25)

certo = randint(0, 10)
cont = 0
acertou = False
while not acertou:
    p = int(input('Adivinhe em que número de 0 a 10 eu pensei...'))
    cont += 1
    if p == certo:
        print('Parabéns! Você acertou!')
        acertou = True
    else:
        if p > certo:
            print('ERROOOOOU!!!! Tente um número menor!!!')
        elif p < certo:
            print('ERROOOOOU!!!! Tente um número maior!!!')
print(f'Você precisou de {cont} tentativas para acertar o número {certo}!')