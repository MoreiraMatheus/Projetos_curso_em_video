matriz = [[], [], []]
pares = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        add = int(input(f'Digite um numero para [{linha}, {coluna}]: '))
        if add % 2 == 0:
            pares += add
        matriz[linha].append(add)
terlinha = matriz[0][2] + matriz[1][2] + matriz[2][2]
for m in matriz[1]:
    if m > maior:
        maior = m
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print(f'A soma de todos os pares foi {pares}')
print(f'A soma dos valores da 3ª linha foi {terlinha}')
print(f'O maior valor da segunda linha é {maior}')
