#  Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade} - Profissão: {self.profissao}'
    
    def aniversario(self):
        self.idade += 1

    def saudação(self):
        if self.profissao:
            return f'Olá, me chamo {self.nome}! Trabalho como {self.profissao}'
        else:
            return f'Olá, me chamo {self.nome}!'
    

pessoa1 = Pessoa(nome='Carlos', idade = 45, profissao='Bombeiro')
pessoa2 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa3 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa4 = Pessoa(nome='Jaque', idade=22)

print('Bem vindos(as)')
print(pessoa1)
print(pessoa2)
print(pessoa3)
print(pessoa4)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudação())
print(pessoa2.saudação())
print(pessoa3.saudação())
print(pessoa4.saudação())


        
        
