pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 78.5
for k, v in pessoas.items():
    print(f'{k} = {v}')