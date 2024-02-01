i = int(input('Início:'))
r = int(input('Razão:'))
decimo = i + (10 - 1) * r # Fórmula do décimo termo da PA
for c in range(i , decimo + r, r):
    print(c, end=' - ')
print('Acabou!')