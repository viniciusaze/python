from time import sleep

def contador (i, f, p):
    print('-=' * 20)
    if p < 0:
        p *= -1 # para transformar em postitivo
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(1.5)
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)