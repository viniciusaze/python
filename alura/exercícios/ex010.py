#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
try:
    for n in numeros:
            soma += n
    print(f'A soma de todos os números é de {soma}')
except:
      print('Ocorreu um erro!')
