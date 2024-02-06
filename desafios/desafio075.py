n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o último valor: '))
tupla = (n1, n2, n3, n4)
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 aparece na posição {tupla.index(3)+1}.')
else:
    print('O numero 3 não apareceu nenhuma vez.')
print('Os valores PARES foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(f'{n}', end=' ')

#valores = tuple(int(input('Digite valores '))for c in range(1, 5))
#print(f'O numero nove aparece {valores.count(9)} vezes')
#print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else 'Não foi digitado valor 3')
#print('Valores pares digitados foram', end=' ')
#print({n for n in valores if n % 2 == 0}, end=' ')