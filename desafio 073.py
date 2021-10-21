classificados = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
                 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino',
                 'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife',
                 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print('='*40 + '\nClassificados do Brasileirão 06/03/2021\n' + '='*40)
print('Os 5 primeiros colocados são:')  # os 5 primeiros colocados
for c in range(0, 5):
    print('\033[34m', classificados[c], '\033[m')

print('\nOs quatro ultimos são:')  # os 4 ultimos colocados
for c in range(16, 20):
    print('\033[31m', classificados[c], '\033[m')

print('\nOs 20 colocados em ordem alfabética ficariam:')  # todos os times em ordem alfabética
linha = 0
for c in range(0, 20):
    linha += 1
    print('\033[33m', sorted(classificados)[c], end='\033[m, ')
    if linha == 5:
        print('\n', end='')
        linha = 0

time = input('\nEscolha um time: ').strip().capitalize()  # Procurar um time
if time in classificados:
    print(f'Este time está em \033[32m{classificados.index(time)+1}\033[m colocado')
else:
    print('este time não está entre os 20 colocados do brasileirão.')
