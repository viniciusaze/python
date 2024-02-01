n1 = float(input('Informe o valor da primeira reta: '))
n2 = float(input('Informe o valor da segunda reta: '))
n3 = float(input('Informe o valor da terceira reta: '))

if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n2 + n1):
    if n1 == n2 and n2 == n3 and n3 == n1:
        print('Triângulo Equilátero:\nTodos os lados são iguais') 
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Triângulo Isóceles:\nDois lados iguais') 
    elif n1 != n2 or n2 != n3 or n3 != n1:
        print('Triângulo Escaleno:\nTodos os lados diferentes')
else:
    print('As retas não formam um triângulo!')
    
