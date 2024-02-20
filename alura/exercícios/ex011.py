#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

valores = [5, 2, 8, 1, 9, 2]
soma = media = 0
c = 1
for numero in valores:
    soma += numero
    c += 1
try:
    media = soma / c
    print(f'A média dos valores é {media:.2f}')
except ZeroDivisionError:
    print('ERRO! Lista vazia')
except Exception as e:
    print(f'ERRO! {e}')

