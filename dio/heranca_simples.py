class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando o motor')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) # Método para sobrescrever as caracteristicas
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{'Sim' if self.carregado else 'Não'}')

moto = Motocicleta('preta', 'abc-1234', 2)

carro = Carro('branco', 'xcd-0921', 4)

caminhao = Caminhao('vermelho', 'rej-8153', 8, False)

print(moto)
print(carro)
print(caminhao)