from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): # Para herdade metodos, atributos de outra classe
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) # super acessa informações de outra classe, no caso a ItemCardapio
        self.descricao = descricao