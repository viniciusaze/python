import math
a = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print(f'O ângulo informado foi de {a}°.\nSeu seno: {sen:.2f}.\nSeu cosseno: {cos:.2f}.\nSua tangente: {tan:.2f}')