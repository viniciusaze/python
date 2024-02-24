from ex027 import Livro

# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.


livro1 = Livro('O Maluco Doido', 'Mario Pitanga', 1995)
print(f'Livro {livro1._titulo} disponível? -> {livro1.disponivel}')
livro1.emprestar()
livro2 = Livro('Floresta Negra', 'Elba Garcia', 2001)

ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")
