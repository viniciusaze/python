frase = input('Digite uma frase: ').strip().upper()
frasediv = frase.split()
junto = ''.join(frasediv)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('Palíndromo')
else:
    print('Não é palíndromo.')