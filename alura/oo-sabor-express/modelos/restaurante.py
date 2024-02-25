from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False # O _ é usado para informar que o atributo deve ser protegido, usado como uma boa prática
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self): #Forma de exibir o objeto em forma de texto
        return f'{self._nome} | {self._categoria}'
    
    #Self é a referência daquilo que esta sendo usado no momento
    
    @classmethod # sempre usar quando tiver um método relacionado a classe
    def listar_restaurantes(cls): # Usar o cls no classmethod
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property 
    #property pega um ativo/atributo e altera a forma como vai ser lido, usado quando se deseja somente para leitura. Quando for property, nao precisa () ao execurtar no app
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo # not inverte o estado

    def receber_avaliacao(self, cliente, nota):
        #if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return f'-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = (soma_das_notas / quantidade_de_notas)
        media5 = round(media / 2, 1)
        return media5
    
    #def adicionar_bebida_no_cardapio(self, bebida):
    #    self._cardapio.append(bebida)

    #def adicionar_prato_no_cardapio(self, prato):
    #    self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): #isinstace, pega o item e compara com o ItemCardapio. A função isinstance vai ser verdadeira se o item que passamos como argumento for uma instancia da classe itemcardapio ou derivada
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço R$ {item._preco:.2f} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                menssagem_bebida = f'{i}. Nome: {item._nome} | Preço R$ {item._preco:.2f} | Tamanho: {item.tamanho}'
                print(menssagem_bebida)
            # hasattr para checar se tem o atributo 'descricao' no item
                



