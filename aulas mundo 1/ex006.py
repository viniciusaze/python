n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divi = n1 // n2
pot = n1 ** n2
print(f'Os dois números informados foram: {n1} e {n2}. \n A soma vale {soma}\n A subtração é {sub}\n A multiplicação é {mult}\n a divisão é {div:.3f}\n A divisão inteira é {divi}\n A potência é {pot}!')

# O .3f indica que teremos 3 casas decimais no número
# \n quebra a linha
# end=' ' para não quebrar a linha entre dois prints