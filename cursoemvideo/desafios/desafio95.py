time = []
jogador = {}
partidas = []

# DADOS

while True:
    jogador.clear()
    jogador['nome'] = input('Nome: ')
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas) # SUM = SOMA
    time.append(jogador.copy())
    while True:
        res = input('Quer continuar? [S/N] ').upper()[0]
        if res in 'SN':
            break
        print('ERRO! Responda com S ou N.')
    if res == 'N':
        break

# RESULTADOS
    
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
print('-' * 50)
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)

# ANOSTRAGEM

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'---- LEVANTAMENTO DO JOGADOR {time[busca]['nome']} ----')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   Na {i+1}ª partida fez {g} gols.')
    print('-' * 40)
print('<<<< Volte Sempre >>>>')