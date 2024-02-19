from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 9:
    print(f'Sua categoria: MIRIM')
elif idade >= 9 and idade <= 14:
    print(f'Sua categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'Sua categoria: JUNIOR')
elif idade >19 and idade <= 25:
    print(f'Sua categoria: SÊNIOR')
else:
    print(f'Sua categoria: MASTER')