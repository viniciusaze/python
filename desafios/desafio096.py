def linha():
    print('-' * 30)

def area(a, b):
    area = l * c
    print(f'A área de um terreno de {a}x{b} é de {area:.2f}m²')
linha()
print(' > Controle de Terrenos < ')
linha()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)