from datetime import date

def voto():
    idade = date.today().year - anonasc
    if idade < 16:
        return print(f'Com {idade} anos: VOTO NEGADO.')
    if idade >= 16 and idade < 18 or idade >= 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')

print('-' * 30)
anonasc = int(input('Em que ano você nasceu? '))
voto()