from datetime import date
anoatual = date.today().year
dic = {}
dic['nome'] = input('Nome: ')
idade = int(input('Ano de nascimento: '))
dic['idade'] = anoatual - idade
dic['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dic['ctps'] == 0:
    print('-=' * 35)
    print(f'O nome tem o valor {dic['nome']}')
    print(f'A idade tem o valor {dic['idade']}')
    print(f'CPTS tem o valor {dic['ctps']}')
else:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salário'] = float(input('Salário: R$ '))
    dic['aposentadoria'] =  35 - (anoatual - dic['contratação'])

    print('-=' * 35)
    print(f'O nome tem o valor {dic['nome']}')
    print(f'A idade tem o valor {dic['idade']}')
    print(f'CPTS tem o valor {dic['ctps']}')
    print(f'O ano de contratação tem o valor {dic['contratação']}')
    print(f'O salário é de {dic['salário']}')
    print(f'Faltam {dic['aposentadoria']} anos para se aposentar.')
