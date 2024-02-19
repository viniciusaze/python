primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} -', end=' ')
        termo = termo + razao
        c += 1    
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrado!')