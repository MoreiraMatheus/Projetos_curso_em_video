from random import randint
from time import sleep
jogos = list()
print('='*30, '\nO apostador da mega sena 3000\n' + '='*30)
quant = int(input('Quantos jogos deseja fazer?: '))
for c in range(0, quant):
    jogo = []
    for num in range(0, 6):
        while True:
            add = randint(1, 60)
            if add not in jogo:
                jogo.append(add)
                break
    jogos.append(jogo)
jogos.sort()
for pos, c in enumerate(jogos):
    print(f'Jogo{pos+1}: {c}')
    sleep(0.5)
print('Boa sorte!')
