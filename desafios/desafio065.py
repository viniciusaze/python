maior = 0
menor = 0
soma = 0
c = 0
media = 0
res = 'Y'
while res == 'Y': #ou res in 'Yy'
    n = int(input('Digite um número: '))
    res = input('Deseja continuar? [Y/N]').strip().upper()[0]
    print('^' * 15)
    c += 1
    soma = (soma + n)
    
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n 
        if n < menor:
            menor = n
media = soma / c           
print(f'A média entre os valores digitados foi de {media:.2f}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
print('Fim do programa!')
