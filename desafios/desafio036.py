preco = float(input('Informe o valor do imóvel: R$'))
sal = float(input('Informe o seu salário: R$'))
anos = int(input('Informe em quantos anos irá pagar: '))
prestação = preco / (anos * 12)

print('Calculando a aprovação da compra.')
if prestação > (sal * 30) / 100:
    print('Compra \033[1;31mREPROVADA!\033[m Seu salário não cobre os \033[1;31m30%\033[m da parcela!')
elif prestação <= (sal * 30) / 100:
    print(f'Compra \033[1;32mAPROVADA!\033[m\nValor da parcela:  \033[1;32mR${prestação:.2f}\033[m\nQuantidade de parcelas:  \033[1;32m{anos * 12}\033[m')