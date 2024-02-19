def teste():
    x = 8 # Variável de escopo LOCAL
    print(f'Na função teste n vale {n}')
    print(f'Na funcação teste x vale {x}')


# Programa principal
    
n = 2 # Variável de escopo GLOBAL
print(f'No programa principal n vale {n}')
teste()