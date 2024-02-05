n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma de todos os números vale: {s}')

# Desta forma, o break aciona antes da soma, não somando a flag -> 999