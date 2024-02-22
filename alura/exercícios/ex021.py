# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    restaurantes = []

    def __init__(self, nome='', categoria='', ativo=False, capacidade=0, nota=0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota = nota

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.capacidade} | {self.nota}'
    

restaurante1 = Restaurante(nome='Comida Brasileira', categoria = 'Brasileira', ativo=True, capacidade = 57, nota = 8.7)

print(restaurante1)
    

