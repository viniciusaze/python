# Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

class ClienteBanco:
    def __init__(self, nome='', idade='', renda=0, saldo=0, ativo=False):
        self.nome = nome
        self.idade = idade
        self.renda = renda
        self.saldo = saldo

    def __str__(self):
        return f'Dados do cliente: {self.nome} | Idade: {self.idade} | Renda: {self.renda} | Saldo: {self.saldo}'


cliente1 = ClienteBanco('Marcelo', 24, 3000, 5500)
cliente2 = ClienteBanco('Paulo', 56, 4780, 23000)
cliente3 = ClienteBanco('Gabriela', 49, 7800, 15000)

print(cliente1)