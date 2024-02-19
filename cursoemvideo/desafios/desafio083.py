expr = input('Expressão: ')
pilha = []
for simb in expr: # Expressão para chegar os itens dentro da expressão
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() # Remove o último elemento
        else:
            pilha.append(')')
            break
if len(pilha) > 0:
    print('Sua expressão está errada')
else:
    print('Sua expressão está correta!')