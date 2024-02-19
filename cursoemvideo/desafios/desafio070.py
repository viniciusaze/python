nome = ''
barato = ''
preço = tot = cont = contmil = menor = 0

print('-=' * 20)
print('LOJA MAIS BARATA')
print('-=' * 20)

while True:
    nome = input('Nome do Produto: ').strip().capitalize()
    preço = float(input('Preço: R$'))
    cont += 1
    if preço > 1000:
        contmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    tot += preço
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('-*' * 20)
print(f'O total gasto foi: R${tot:.2f}')
print(f'Ao todo foram {contmil} produtos acima de R$1000')
print(f'O produto mais barato foi {barato} custa R${menor}')