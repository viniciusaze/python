frase = input('Digite uma frase: ').strip().upper()
print(f'A letra "a" aparece {frase.count('A')} vezes')
print(f'A letra "a" apareceu na posição {frase.find('A') + 1}')
print(f'A úlima letra "a" apareceu na posição {frase.rfind('A') + 1}')