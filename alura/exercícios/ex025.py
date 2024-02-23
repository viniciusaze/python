# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

# Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

class ContaBancaria:
    def __intit__(self, titular='', saldo=0, ativo=False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: R${self.saldo} | Status da conta: {self.ativo}'
    

pessoa1 = ContaBancaria('Vinícius', 45000)
pessoa2 = ContaBancaria('Fernanda', 50000)

print(pessoa2)
print(pessoa1)

