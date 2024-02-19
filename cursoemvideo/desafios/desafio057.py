sexo = input('Informe seu sexo: [M/F] ').upper().strip()[0]
while sexo not in 'MF':
    sexo = input('Dados inválidos, po favor informe seu sexo [M/F] ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')