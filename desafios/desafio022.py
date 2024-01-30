nome = input('Informe seu nome: ').strip()
dividido = nome.split()
junto = ''.join(dividido)
print(f'Nome em letras maiúsculas: {nome.upper()}')
print(f'Nome em letras minúsculas: {nome.lower()}')
print(f'Quantidade de letras ao total: {len(junto)}')
print(f'Quantidade de letras no primeiro nome: {len(dividido[0])}')

#print(f'Quantidade de letras ao total: {len(nome) - nome.count(' ')}') 
#print(f'Quantidade de letras no primeiro nome: {nome.find(' ')}')
#Outros jeitos de fazer