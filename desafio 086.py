matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Digite um numero para a {linha} linha, coluna {coluna}: ')))
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
