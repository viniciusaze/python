preco = float(input('Informe o valor do produto: R$'))
cond = input('''Qual a condição de pagamento? 
1 - À vista dinheiro / cheque
2 - À vista cartão
3 - 2x no cartão
4 - 3x ou mais no cartão
Qual a opção? ''').strip().lower()


if cond == '1':
    desc = (preco * 10 / 100)
    print(f'Valor com 10% de desconto: R${preco - desc}')
elif cond == '2':
    desc = (preco * 5 / 100)
    print(f'Valor com 5% de desconto: R${preco - desc}')
elif cond == '3':
    print(f'Valor do produto sem desconto: R${preco}')
    print(f'Valor das parcelas: {preco /2 }')
elif cond == '4':
    juros = (preco * 20 / 100)
    qntpar = int(input('Quantas parcelas? '))
    valpar = (preco + juros) / qntpar
    print(f'Valor do produto com acrescimo do cartão: R${juros + preco}')
    print(f'Quantidade de parcelas: {qntpar}')
    print(f'Valor das parcelas: {valpar}')
else:
    print('Informe um valor válido.')