vel = float(input('Informe a velocidade medida: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Velocidade acima da permitida! MULTADO!')
    print(f'Valor da multa: R${multa:.2f}')
else:
    print('Velocidade permitida.')
print('Tenha um bom dia, dirija com segurança!')