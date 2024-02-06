a = [2, 3, 4, 7]
#b = a  Não é cópia de lista, e sim uma ligação, se mudar uma, muda a outra
b = a[:] # Forma de criar cópia de lista
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')