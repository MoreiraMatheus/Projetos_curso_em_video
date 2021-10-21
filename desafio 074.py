from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for c in range(0, len(numeros)):
    print(numeros[c], end=' ')
print(f'\nO maior valor é {max(numeros)}\nO menor valor é {min(numeros)}')
