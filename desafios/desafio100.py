from random import randint
from time import sleep

def sorteio(listas):
    print(f'Sorteando os 5 valores:')
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        sleep(0.3)
        print(f'{n} ', end='', flush=True)
    print('Pronto!!!')

def somaPar(listas):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []
sorteio(numeros)
somaPar(numeros)

numeros.clear()

num = []
sorteio(num)
somaPar(num)

