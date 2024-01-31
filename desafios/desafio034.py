s = float(input('Qual o seu salário?' ))
if s < 1250:
    aumento = (s * 15) / 100
    print(f'Com o aumento, seu salário será de R${aumento + s:.2f}')
else:
    aumento = (s * 10) / 100
    print(f'Com o aumentor, seu salário será de R${aumento + s:.2f}')