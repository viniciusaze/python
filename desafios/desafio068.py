from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)


cont = 0

while True:
    jog = int(input('Diga um valor: '))
    parimp = (input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    pc = randint(1, 10)
    while parimp not in 'PpIi':
        parimp = (input('Par ou Ímpar? [P/I]')).strip().upper()[0]

    if (jog + pc) % 2 == 0:
        if parimp == 'P':
            print(f'Você jogou {jog} e o computador {pc}. Total de {pc + jog} deu PAR')
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        if parimp == 'I':
            print(f'Você jogou {jog} e o computador {pc}. Total de {pc + jog} deu ÍMPAR')
            print('Você PERDEU')
            print('=-' * 20)
            break
    if (jog + pc) % 2 != 0:
        if parimp == 'P':
            print(f'Você jogou {jog} e o computador {pc}. Total de {pc + jog} deu ÍMPAR')
            print('Você PERDEU')
            print('=-' * 20)
            break
        if parimp =='I':
            print(f'Você jogou {jog} e o computador {pc}. Total de {pc + jog} deu ÍMPAR')
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
print(f'GAME OVER! Você venceu {cont} vezes')