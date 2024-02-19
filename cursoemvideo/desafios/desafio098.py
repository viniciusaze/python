from time import sleep

def linha():
    print('-=' * 15)

def contador(i, f, p):

    for c in range(inicio, fim +1, passo):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('Fim!')

def contadorvolt(a, b):
    for c in range(inicio, fim - 1, - passo):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('Fim!')

inicio =  1
fim = 10
passo = 1
linha()
print('Contagem de 1 até 10 de 1 em 1.')
contador(inicio, fim, passo)

inicio = 10
fim = -3
passo = -2
linha()
print('Contagem de 10 até 0 de 2 em 2.')
contador(inicio, fim, passo)

linha()
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
if inicio > fim:
    linha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    contadorvolt(inicio, fim)
else:
    linha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    contador(inicio, fim)
