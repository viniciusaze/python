class Estudante:
    escola = 'DIO' # Atributo de classe

    def __init__(self, nome, matricula):
        # Atributos de instancia
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'


def mostrar_matricula(*objeto):
    for obj in objeto:
        print(obj)


aluno1 = Estudante('Vinicius', 200608) 
aluno2 = Estudante('Fernanda', 201008)

mostrar_matricula(aluno1, aluno2)

# Trocando atributos de instancia
aluno1.matricula = 200612

mostrar_matricula(aluno1, aluno2)

# Trocando atributos de classe
Estudante.escola = 'Python'

mostrar_matricula(aluno1, aluno2)