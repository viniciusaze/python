palavras = ('casa', 'cachorro', 'computador', 'banana', 'suco', 'mesa', 'mouse', 'aprender', 'curso')

for pos in palavras: # Para as palavras na tupla
    print(f'\nNa palavra {pos.capitalize()} temos: ', end='')
    for letra in pos: # Para as letras na palavra
        if letra.lower() in 'aeiou':
            print(letra, end=' ')