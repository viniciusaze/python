galera = []
dado = []
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Copiou o dado e colocou na galera
    dado.clear() # Para apagar o dado
print(galera)
for p in galera:
    print(f'Usuário:{p[0]}')
    print(f'Idade: {p[1]}')
    print('-~' * 10)
c = 0
for p in galera:
    if p[1] >= 21:
        c += 1
print(f'Ao todo temos {c} usuários com mais de 21 anos')