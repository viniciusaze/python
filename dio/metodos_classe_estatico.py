class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod # Criando método de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome): # Utiliza-se o cls ao invez do self
        idade = 2024 - ano
        return cls(nome, idade)
    # Se precisar ter acesso ao contexto da classe, usar o metodo de classe
    
    @staticmethod # Criando método estático
    def maior_de_idade(idade):
        return idade >= 18
    # Se não precisar acesso nem ao contexo da classe e nem da instancia do objeto, usar metodo estatico

# p = Pessoa('Vinicius', 28)
# print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(1995, 7, 27, 'Vinicius')
print(p2.nome, p2.idade)

print(Pessoa.maior_de_idade(18))
print(Pessoa.maior_de_idade(8))