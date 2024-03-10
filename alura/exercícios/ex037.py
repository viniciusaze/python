# 8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

from random import choice

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

fruta1 = choice(frutas)
fruta2 = choice(frutas)
while fruta1 == fruta2:
    fruta2 = choice(frutas)
fruta3 = choice(frutas)
while fruta3 == fruta2 or fruta3 == fruta1:
    fruta3 = choice(frutas)

print(f'Sua salada de frutas surpresa: {fruta1}, {fruta2} e {fruta3}')
