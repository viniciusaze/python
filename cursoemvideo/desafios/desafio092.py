from datetime import date
anoatual = date.today().year
dic = {}
dic['nome'] = input('Nome: ')
idade = int(input('Ano de nascimento: '))
dic['idade'] = anoatual - idade
dic['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dic['ctps'] == 0:
    print('-=' * 35)
    for k, v in dic.items():
        print(f'{k} tem o valor {v}')
else:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salário'] = float(input('Salário: R$ '))
    dic['aposentadoria'] = dic['idade'] + ((dic['contratação'] + 35) - anoatual)

    print('-=' * 35)
    for k, v in dic.items():
        print(f'{k} tem o valor {v}')
