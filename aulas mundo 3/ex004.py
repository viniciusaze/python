num = [2, 5, 9 ,1]
num[2] = 3 # Substitui um item da posição 2 da lista
num.append(7) # Adiciona um item ao final da lista
num.sort(reverse=True) # Organiza em ordem reversa
num.insert(2, 0) # Adiciona o numero 0 na posição 2
#num.pop()  Elimina o último valor (Se não tiver nada dentro dos ())
num.insert(2, 2)
#num.remove(2)  Remove o primeiro numero 2 da encontrado 
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')