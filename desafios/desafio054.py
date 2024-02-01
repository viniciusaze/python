from datetime import date
ano = date.today().year
for c in range(1, 8):
    input('Ano de nascimento: ')
    if (ano - c) >= 21:
        print('Maior idade')