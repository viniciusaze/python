print('-=' * 15)
print('Análisador de Triângulos')
print('-=' * 15)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2):
    print('Os segmentos PODEM FORMAR um triângulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')