nome = input('Digite seu nome completo: ').strip()
nomediv = nome.split()
print(f'Primeiro nome: {nomediv[0]} ')
print(f'Último nome: {nomediv[len(nomediv)-1]}')