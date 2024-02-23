class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo.ljust(20)} por {self.autor.ljust(20)} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

livro1 = Livro(titulo='Aventuras', autor='Monteiro Lobato', paginas=357)
livro2 = Livro(titulo='Memórias', autor='Chico Escritor', paginas=298)
livro3 = Livro(titulo='Diário', autor='Lisandra Silva', paginas=1054)

print('Informações sobre os livros')
print(f'{'Título'.ljust(20)} {'Autor'.ljust(20)}     Páginas')
print(livro1)
print(livro2)
print(livro3)
