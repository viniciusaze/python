# 3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

from random import choice

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

sorteado = choice(lista)
print(sorteado)

# 4. Crie um programa que sorteia, aleatoriamente, um número inteiro menor que 100.
# Dica: use a função randrange() da biblioteca random. Essa função recebe como parâmetro o valor limite para a escolha aleatória ou um intervalo se passado o limite mínimo e máximo. Por exemplo, randrange(5) gera valores inteiros menores que 5.

from random import randrange

sorteio = randrange(100)
print(f'Número sorteado: {sorteio}')
