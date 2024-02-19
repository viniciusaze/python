estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = input('Unidade federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy()) # Para copiar a informação
for e in brasil:
    print(f'Estado {e['uf']}, sigla {e['sigla']}')