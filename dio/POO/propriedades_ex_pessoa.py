class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    

pessoa = Pessoa('Vinicius', 1995)
print(f'Nome: {pessoa.nome} \tIdade: {pessoa.idade}') 
#Note que as property não usam os (), pois não são metodos e sim propriedades