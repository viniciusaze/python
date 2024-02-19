from datetime import date
ano = date.today().year
contmaior = 0
contmenor = 0
for c in range(1, 8):
    anonasc = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    idade = ano - anonasc
    if idade >= 18:
        contmaior += 1
    else:
        contmenor +=1
print(f'Ao total ,{contmaior} pessoas são maiores de idade e {contmenor} são menores de idade.')
