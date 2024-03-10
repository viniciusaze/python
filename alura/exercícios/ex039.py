# 9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:
from math import sqrt
numeros = [2, 8, 15, 23, 91, 112, 256]

# No final, informe quais números possuem raízes inteiras e seus respectivos valores.

for n in numeros:
    raiz = sqrt(n)
    print(f'Raiz de {n} = {raiz:.2f} é inteiro? :', raiz // 1 == raiz)