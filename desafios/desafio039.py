from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano

if idade > 18:
    print(f'Você ja passou {idade - 18} ano(s) do ano de alistamento!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} ano(s) para você se alistar!')
elif idade == 18:
    print(f'Você está na idade de se alistar, procure a junta militar da sua cidade!')