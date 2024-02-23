# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

# Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

# Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

# Crie uma instância da classe e imprima o valor da propriedade titular.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self._titular} | Saldo: R${self._saldo} | Status da conta: {self._ativo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo= True

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    

conta1 = ContaBancaria('Vinícius', 150000)
ContaBancaria.ativar_conta(conta1)
conta2 = ContaBancaria('Fernanda', 200000)
conta3 = ContaBancariaPythonica('Luis', 4000)

print(conta1)
print(conta2)
print(f'Titular da conta 3: {conta3.titular}')