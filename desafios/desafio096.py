def linha():
    print('-' * 30)

def area(a, b):
    a = l * c
    print(f'A área de um terreno de {l}x{c} é de {a:.2f}m²')
linha()
print(' > Controle de Terrenos < ')
linha()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)