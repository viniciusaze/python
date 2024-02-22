# 1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

# 2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

nome_do_restaurante = restaurante_praca.nome

print(nome_do_restaurante)

# 3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

print(f'O Restaurante {nome_do_restaurante} está ativo') if restaurante_praca.ativo else print(f'O restaurante {nome_do_restaurante} está inativo')

# 4. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.

categoria = Restaurante.categoria

# 5. Altere o valor do atributo nome para 'Bistrô'.

restaurante_praca.nome = 'Bistrô'

# 6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

# FEITA ACIMA

# 7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

# 8. Mude o estado da instância restaurante_pizza para ativo.
    
# FEITA ACIMA
    
# 9. Imprima no console o nome e a categoria da instância restaurante_praca.
    
print(f'Nome do restaurante: {restaurante_praca.nome}')
print(f'Categoria: {restaurante_praca.categoria}')
