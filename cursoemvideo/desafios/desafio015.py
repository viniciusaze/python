d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))
ppd = d * 60
ppkm = km * 0.15
total = ppd + ppkm
print(f'O preço total a ser pago é de: R${total:.2f}.\n(Km -> R${ppkm:.2f})\n(Dias -> R${ppd:.2f})')