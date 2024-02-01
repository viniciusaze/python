n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'\033[4;30;41mREPROVADO!\033[m Sua média foi de {media:.2f}.')
elif media >= 7:
    print(f'\033[4;30;42mAPROVADO!\033[m Sua média foi de {media:.2f}.')
else:
    print(f'\033[4;30;44mRECUPERAÇÃO!\033[m Sua média foi de {media:.2f}.')