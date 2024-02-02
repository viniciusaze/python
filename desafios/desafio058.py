from random import randint
print('~' * 25)
print('JOGO DA ADVINHAÇÃO 2.0')
print('~' * 25)

certo = randint(0, 10)
cont = 0
p = 99
while p != certo:
    p = int(input('Adivinhe em que número de 0 a 10 eu pensei...'))
    print('ERROOOOOOOU KKKKK')
    cont += 1
    if p == certo:
        print('Parabéns! Você acertou!')
print(f'Você precisou de {cont} tentativas para acertar!')