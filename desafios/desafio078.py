lista = []
mai = 0
men = 0
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
     
print('-=' * 20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é de {mai} e esta na posição', end=' ')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}', end='...')
print()
print(f'O menor valor da lista é de {men} e está na posição,', end=' ')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}', end='...')
