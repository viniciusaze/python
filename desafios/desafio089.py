boletim = []
nome = []
notas = []
while True:
    nome.append(input('Nome: ').strip())
    boletim.append(nome[:])
    nome.clear()
    notas.append(float(input('Nota 1:')))
    notas.append(float(input('Nota 2:')))
    boletim.append(notas[:])
    notas.clear()
    res = input('Quer continuar? [S/N]').upper().strip()
    if res == 'N':
        break
    else:
        while res != 'S':
            res = input('Quer continuar? [S/N]').upper().strip()
print('-=' * 40)

        
