class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # Usa-se o _ por convenção para indicar que o atributo é privado
        self.nro_agencia = nro_agencia # Atributo publico
    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    # Forma correta de acessar um atributo privado, por métodos
    def mostrar_saldo(self):
        # ...
        return self._saldo

conta = Conta('0001', 100)
# Não utilizar dessas forma, pois o atributo é privado
# conta._saldo += 100
# print(conta._saldo)

# Utilizar os métodos da maneira correta
conta.depositar(100)

print(conta.nro_agencia)
print(conta.mostrar_saldo())