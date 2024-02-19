lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') 

# Tuplas podem estar entre parênteses ou não
# Tuplas são IMUTÁVEIS

#print(lanche)

for c in lanche:
    print(f'{c}') # Nesse modelo não conseguimos mostrar a posição do item

# Nesses modelos de baixo conseguimos mostrar a posição do item

for c in range(0, len(lanche)):
    print(f'Eu vou comer {c} na posição {c}')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')

# Duas tecnicas de mostrar os itens em repetição for