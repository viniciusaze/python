n = c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if n < 0:
        break
    for c in range(0,10):
        c += 1
        tab = n * c
        print(f'{n} x {c} = {tab}')
    print('-' * 20)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')