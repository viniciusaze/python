km = int(input('Qual a distância da viagem em Km? '))
if km < 200:
    menor = km * 0.5
    print(f'A sua viagem de {km}Km, custará R${menor:.2f}.')
else:
    maior = km * 0.45
    print(f'A sua viagem de {km}Km, custará R${maior:.2f}.')