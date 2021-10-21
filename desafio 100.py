from random import randint
from time import sleep

numeros = []


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Sorteando 5 valores: ', end='')
    for c in lista:
        sleep(0.3)
        print(c, end=' ')
    print('Pronto')


def somapar(lista):
    pares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    if len(pares) == 0:
        print('Nenhum numero par foi sorteado.')
    else:
        print(f'Os numeros pares foram: {pares}, somando todos temos {sum(pares)}')


sorteia(numeros)
somapar(numeros)
