primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
res = 0
while c < 10:
    res =  (primeiro + razao)
    fat = res + razao
    c += 1
    print(f'{fat}', end=' - ')