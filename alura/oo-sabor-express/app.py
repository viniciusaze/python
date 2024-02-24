from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()