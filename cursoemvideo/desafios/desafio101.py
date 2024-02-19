def voto(ano):
    from datetime import date #Importação de escopo, só vale dentro da função

    idade = date.today().year - ano
    if idade < 16:
        return print(f'Com {idade} anos: VOTO NEGADO.')
    if idade >= 16 and idade < 18 or idade > 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    

# Programa principal
print('-' * 30)
anonasc = int(input('Em que ano você nasceu? '))
voto(anonasc)