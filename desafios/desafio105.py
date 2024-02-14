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
    dic['situação'] = 'BOA', 'RUIM', 'RAZOÁVEL'
    if media < 6:
        sit =dic['situação'][1]
    if media >=6 and media < 7:
        sit = dic['situação'][2]
    else:
        sit = dic['situação'][0]
    return dic

res = notas(3.5, 2, 6.5)
print(res)