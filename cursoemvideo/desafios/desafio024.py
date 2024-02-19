cidade = input('Digite o nome de uma cidade: ').strip()

print(f'Sua cidade começa com a palavra santo? {cidade[:5].upper() == 'SANTO'}')