from random import randint
numeros = []

def sorteio():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print(f'Sorteando os 5 valores: {numeros}, PRONTO!')


def somaPar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')

sorteio()
somaPar(numeros)

