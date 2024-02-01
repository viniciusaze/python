nome = input('Qual é o seu nome? ').strip().lower()
if nome == 'vinicius':
    print('Eai meu chará')
elif nome == 'fernanda':
    print('Que lindo nome')
elif nome == 'bilu' or nome == 'mel':
    print('Nome de cachorros doidos')
else:
    print('Nome sem graça...')
print(f'Tenha um bom dia, {nome.capitalize()}')

# Estrutura condicional aninhada !