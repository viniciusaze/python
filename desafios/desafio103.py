def ficha(n, g):
    if n == '':
        n = '<desconhecido>'
    if g == '':
        g = 0
    return print(f'O jogador {n} fez {g} gol(s) no campeonato.')

print('-' * 20)
nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
ficha(nome, gols)