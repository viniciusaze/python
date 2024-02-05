print('-' * 20)
print('CADASTRO')
print('-' * 20)
idade = 0
sexo = ''
continuar = ''
maior18 = 0
sexm = 0
mm20 = 0
while True:
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior18 += 1
    sexo = input('Sexo: [M/F] ').strip().upper()
    if sexo == 'M':
        sexm += 1
    if sexo == 'F' and idade < 20:
        mm20 += 1
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()
    print('-' * 20)
    continuar = input('Quer continuar? [S/N]').strip().upper()
    if continuar == 'N':
        break
    while continuar not in 'S':
        continuar = input('Quer continuar? [S/N]').strip().upper()
    
        
print('FIM DO PROGRAMA !!!!')
print(f'Total de pessoas com mais de 18 anos: {maior18}') 
print(f'Ao todo temos {sexm} homens cadastrados.')
print(f'E temos {mm20} mulheres com menos de 20 anos.')

