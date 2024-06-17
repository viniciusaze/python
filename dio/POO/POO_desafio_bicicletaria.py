# Criando a classe
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro = 18): # Método construtor
        # Atributos da classe
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
    
    def buzinar(self):
        print('biiiiii biiiii...')

    def parar(self):
        print('Parando a bicileta...')
        print('Bicicleta parada!')

    def correr(self):
        print('Vruuuuuum ...')

    #def __str__(self): #Método para retornar o objeto em string
        #return f'Bicicleta - cor: {self.cor}, modelo: {self.modelo}, ano: {self.ano}, valor: {self.valor}'
    
    # Outra forma, automatizada:
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'
    

b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('verde', 'monark', 2000, 198)
Bicicleta.buzinar(b2) # ou b2.buzinar() são duas chamadas equivalentes

print(b2)


