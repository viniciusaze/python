from abc import ABC, abstractmethod # Importando o modulo a classe ABC

# Classe abstrata / Contrato / Interface
class ControleRemoto(ABC):
    # Métodos Abstratos: é um método que necessariamente não tem um corpo e todas as classes filhas são obrigadas a implementar
    # Quando a classe é abstrata, ela não pode ser instanciada diretamente
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

# Classe filha da classe abstrata obrigatoriamente tem que ter os métodos da classe abstrata
class ControleTV(ControleRemoto):
    def ligar(self):
        print('TV ligada')

    def desligar(self):
        print('TV desligada')


controle = ControleTV()
controle.ligar()
controle.desligar()