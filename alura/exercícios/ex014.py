#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

pessoa = {'nome': 'Luis', 'idade': 36, 'profissão': 'Motorista'}
pesquisar = input('Digite a chave a ser pesquisada: ').lower()
if pesquisar in pessoa:
    print(f'A chave {pesquisar} está no dicionário')
else:
    print(f'A chave {pesquisar} não está no dicionário')