#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0
for n in range(1, 11):
    if n % 2 != 0:
        soma += n
print(soma)
