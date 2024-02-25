from ex028.banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereço, numero):
        super().__init__(nome, endereço)
        self._numero = numero