from random import randint
from time import sleep

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]

print('MEGA SENA')
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'SORTEANDO {jogos} JOGOS')
sleep(1)
for c in range(1, jogos):
    print(f'Jogo {c}: {randint(1, 60, 6)}')
    c += 1