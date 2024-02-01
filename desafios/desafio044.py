preco = float(input('Informe o valor do produto: R$'))
cond = input('Qual a condição de pagamento? (Dinheiro/Cheque)(Cartão)(2x)(3x) ').strip().lower()

if cond == 'dinheiro' or cond == 'cheque':
    desc = (preco * 10 / 100)
    print(f'Valor com 10% de desconto: R${preco - desc}')
elif cond == 'cartão':
    desc = (preco * 5 / 100)
    print(f'Valor com 5% de desconto: R${preco - desc}')
elif cond == '2x':
    print(f'Valor do produto sem desconto: R${preco}')
elif cond == '3x':
    juros = (preco * 20 / 100)
    print(f'Valor do produto com acrescimo do cartão: R${juros + preco}')
else:
    print('Informe um valor válido.')