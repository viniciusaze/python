s = 0 # ACUMULADOR
cont = 0 # CONTADOR
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print(f'A de todos os {cont} valores solicitados é {s}')
