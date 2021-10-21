from time import sleep
from random import randint
from operator import itemgetter
maior = 0
dados = dict()
colocado = 1
input('=== Sorteador de dados. ===\nAperte enter para dar play.')
for c in range(1, 6):
    j = 'Jogador ' + str(c)
    dados[j] = randint(1, 6)
print('='*27 + '\nOs dados sorteados foram:')
for jogador, valor in dados.items():
    print(f'O jogador \033[34m{jogador}\033[m jogou {valor}')
    sleep(0.5)
print('='*27 + f'\n{"Ranking":^27}\n' + '='*27)
rank = sorted(dados.items(), key=itemgetter(1), reverse=True)
for valor in rank:
    print(f'O \033[33m{colocado}º\033[m foi \033[34m{valor[0]}\033[m que jogou {valor[1]}')
    colocado += 1
    sleep(0.5)
