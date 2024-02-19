peso = float(input('Informe seu peso: (kg) '))
alt = float(input('Informe sua altura: (m) '))
imc = peso / (alt**2)

if imc < 18.5:
    print(f'IMC = {imc:.2f}. Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print(f'IMC = {imc:.2f}. Peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'IMC = {imc:.2f}. Sobrepeso.')
elif imc >= 30 and imc < 40:
    print(f'IMC = {imc:.2f}. Obesidade')
else:
    print(f'IMC = {imc:.2f}. Obesidade mórbida')