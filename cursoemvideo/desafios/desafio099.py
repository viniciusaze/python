from time import sleep
def maior(* num):
    print('-=' * 30)
    maior = 0
    tam = len(valores)
    print('Analisando os valores passados...')
    cont = 0
    for v in valores:
        print(f'{v} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = v
        if v > maior:
            maior = v
        cont += 1
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


valores = [2, 9, 4, 5, 7, 1]
maior(valores)
valores = [4, 7, 0]
maior(valores)
valores = [1, 2]
maior(valores)
valores = [6]
maior(valores)
valores = []
maior(valores)
