maior = 0
menor = 0
soma = 0
c = 0
media = 0
res = 'Y'
while res == 'Y':
    n = int(input('Digite um número: '))
    res = input('Deseja continuar? [Y/N]').strip().upper()
    print('^' * 15)
    c += 1
    soma = (soma + n)
    media = soma / c
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n 
        if n < menor:
            menor = n
print(f'A média entre os valores digitados foi de {media}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
print('Fim do programa!')
