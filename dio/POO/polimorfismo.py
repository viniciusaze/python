class Passaro:
    def voar(self):
        print('Voando ...')

class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não pode voar')

# FIXME: Exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print('Avião está decolando...')

# Polimorfismo
def plano_voo(objeto):
    objeto.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
# Objeto se comporta de forma diferente, porem chamando o mesmo nome.