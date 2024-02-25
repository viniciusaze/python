from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass
        
    #@abstractmethod  implica que todas as classes derivadas são obrigadas a seguir essa diretriz; quando dizemos "precisam", é uma exigência real.

    