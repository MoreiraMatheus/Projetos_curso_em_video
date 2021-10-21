from random import randint
itens = ('\033[34mPedra\033[m', '\033[34mPapel\033[m', '\033[34mTesoura\033[m')
pc = randint(0, 2)
print('jokenpo')
player = int(input('''escolha uma das opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
'''))
player = player - 1
print('você escolheu {} e o computador escolheu {}'.format(itens[player], itens[pc]))
if player == 0:# Pedra
    if pc == 0:
        print('EMPATE!')
    elif pc == 1:
        print('DERROTA!')
    elif pc == 2:
        print('VITORIA!')
    else:
        print('JOGADA INVALIDA!')
elif player == 1:# Papel
    if pc == 0:
        print('VITORIA!')
    elif pc == 1:
        print('EMPATE!')
    elif pc == 2:
        print('DERROTA!')
    else:
        print('JOGADA INVALIDA!')
elif player == 2:# Tesoura
    if pc == 0:
        print('DERROTA!')
    elif pc == 1:
        print('VITORIA!')
    elif pc == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')
