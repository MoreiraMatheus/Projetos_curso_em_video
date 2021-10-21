from random import randint

acerto = False
tent = 0
numpc = randint(1, 10)

while not acerto:
    num = int(input('tente adivinhar o numero que estou pensando entre 0 e 10: '))
    tent += 1
    if numpc == num:
        print('\nESSE É O MESMO NUMERO QUE EU PENSEI!!!')
        acerto = True
    else:
        print('kkkk errou otário')
        if num > numpc:
            print('Um pouco menos')
        else:
            print('um pouco mais')
print('Você precisou de \033[36m{}\033[m tentativas para me vencer'.format(tent))
print('---FIM---')
