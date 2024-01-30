from math import hypot
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
res = hypot(ca, co)
print(f'A Hipotenusa calculada tem o valor de {res:.2f}')