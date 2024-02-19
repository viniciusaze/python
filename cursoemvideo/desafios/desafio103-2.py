def ficha(n = '<desconhecido>', g = 0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')

print('-' * 20)
n = input('Nome do jogador: ').strip()
g = input('Número de gols: ')
if g.isnumeric(): #Para saber se é um número
    g = int(g)
else:
    g = 0
if n == '':
    ficha(g = g)
else:
    ficha(n, g)
