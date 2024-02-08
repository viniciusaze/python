jogador = {}
listagol = []
jogador['nome'] = input('Nome do jogador: ')
qnt = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
soma = 0
for c in range(1, qnt + 1):
    gol = int(input(f'Quantos gols na {c}ª partida? '))
    listagol.append(gol)
    soma += gol
    jogador['gols'] = listagol
jogador['total'] = soma
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {qnt} partidas.')
for p in range(1, qnt):
    print(f'Na partida {p}, fez {listagol[p]} gols.')
print(f'Foi um total de {jogador['total']} gols!')
print('>>>> FIM DO PROGRAMA <<<<')
