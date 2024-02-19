def dobro(preço = 0, format=False):
    res = preço * 2
    if format:
        return moeda(res)
    else:
        return res


def metade(preço = 0, format=False):
    res = preço / 2
    if format:
        return moeda(res)
    else:
        return res


def aumentar(preço = 0, taxa = 0, format=False):
    res = preço + ((preço * taxa) / 100)
    if format:
        return moeda(res)
    else:
        return res



def diminuir(preço = 0, taxa = 0, format=False):
    res = preço - ((preço * taxa) / 100)
    if format:
        return moeda(res)
    else:
        return res


def moeda(preço = 0, moeda = 'R$'):
    res = f'{moeda}{preço:.2f}'.replace('.',',') #Substituir . por ,
    return res


def resumo(p, aum, red):
    print('-' * 30)
    print('RESUMO DO VALOR')
    print('-' * 30)
    print('Preço analisado:', end='')
    print(f'{moeda(p)}')
    print('Dobro do preço:' , end='')
    print(f'{moeda(dobro(p))}')
    print('Metade do preço:', end='')
    print(f'{moeda(metade(p))}')
    print(f'{aum}% de aumento:', end='')
    print(f'{moeda(aumentar(p, aum))}')
    print(f'{red}% de redução:', end='')
    print(f'{moeda(diminuir(p, red))}')
    print('-' * 30)
