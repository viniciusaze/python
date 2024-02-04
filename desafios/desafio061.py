primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo} -', end=' ')
    termo = termo + razao
    c += 1
print('FIM')