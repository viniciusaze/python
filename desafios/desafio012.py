preco = float(input('Qual o valor do produto?'))
desc = (preco * 5) / 100
precofinal = preco - desc
print(f'O valor total do produto informado é de R${preco}.\n O valor do desconto de 5% é de R${desc:.2f}.\n O valor final fica em R${precofinal:.2f}.')