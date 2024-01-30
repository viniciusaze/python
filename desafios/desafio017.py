import math
ca = int(input('Digite o valor do cateto adjacente: '))
co = int(input('Digite o valor do cateto oposto: '))
res = math.hypot(ca, co)
print(f'A Hipotenusa calculada é tem o valor de {res:.2f}')