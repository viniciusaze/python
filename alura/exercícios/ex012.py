#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = {'nome': 'Fernanda', 'idade': 20, 'cidade': 'Gravataí'}

#2 - Utilizando o dicionário criado no item 1:

#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.

pessoa['idade'] = 22
pessoa['profissão'] = 'Analista de RH'
del pessoa['cidade']

print(pessoa)