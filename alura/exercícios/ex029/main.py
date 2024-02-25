# Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

# Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

from carro import Carro
from moto import Moto

carro1 = Carro('Corsa', 'Chevrolet', 4)
carro2 = Carro('Prisma', 'Chevrolet', 4)
carro3 = Carro('Strada', 'Fiat', 2)

moto1 = Moto('Z400', 'Kawasaki', 'Esportiva')
moto2 = Moto('CB650', 'Honda', 'Esportiva')
moto3 = Moto('Titan 150', 'Honda', 'Casual')
print('CARROS')
print(carro1)
carro2.habilita_veiculo()
print(carro2)
print(carro3)
print('\nMOTOS')
print(moto1)
print(moto2)
print(moto3)
