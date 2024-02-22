# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome='', idade=int, sexo = '', profissao='',):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.profissao = profissao

    def __str__(self):
        return f'''Nome: {self.nome}
Idade: {self.idade}
Sexo: {self.sexo}
Profissão: {self.profissao}'''


cliente1 = Cliente(nome = 'Maria', idade = 37, sexo = 'Feminino', profissao = 'Advogado(a)')

print(cliente1)