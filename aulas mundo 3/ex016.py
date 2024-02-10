def dobra(lst): # O parâmetro pode ser o que quiser
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [5, 3, 1, 8, 12, 7]
print(valores)
dobra(valores)
print(valores)