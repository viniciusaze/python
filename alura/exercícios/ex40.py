# 10. Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.

from math import pi, pow

raio = float(input('Informe o raio da área: '))

area = pi * pow(raio,2)
custo = area * 25

print(f'O custo para a área de {area:.2f} é de R${custo:.2f}')