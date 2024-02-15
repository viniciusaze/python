def notas(* num, sit=False):
    dic = {}
    cont = s = maior = menor = media = 0
    for nota in num:
        if cont == 0:
            maior = nota
            menor = nota
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        s += nota
        cont += 1
    media = s/cont
    dic['total'] = cont
    dic['maior'] = maior
    dic['menor'] = menor
    dic['media'] = media
    if sit:
        if dic['media'] <= 5:
            dic['situação'] = 'RUIM'
        elif dic['media'] >= 7:
            dic['situação'] = 'BOA'
        else:
            dic['situação'] = 'RAZOÁVEL'
    return dic

resp = notas(8, 7, 6.5, sit=True)
print(resp)