valores = list()
for c in range(0, 5):
    add = int(input('Digite um valor: '))
    if c == 0:
        valores.append(add)
        print('Primeiro valor adicionado.')
    elif add >= max(valores):
        valores.append(add)
        print('Valor adicionado no final da lista.')
    elif add <= min(valores):
        valores.insert(0, add)
        print('Valor adicionado no começo da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if add <= valores[pos]:
                valores.insert(pos, add)
                print('Valor adicionado no meio da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valores}')
