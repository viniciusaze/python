# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    carros = []

    def __init__(self, modelo='', cor='', ano=0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)
    
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'Modelo: {carro.modelo} | Cor: {carro.cor} | Ano: {carro.ano} ')

carro1 = Carro(modelo = 'Corsa', cor = 'Branca', ano = 2006)
carro2 = Carro(modelo = 'Prisma', cor = 'Prata', ano = 2012)
carro3 = Carro(modelo = 'Civic', cor = 'Vermelha', ano = 2020)
    
Carro.listar_carros()