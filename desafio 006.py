valor = float(input('me diga um numero: '))
print('o numero que você escolheu foi: \033[33m{}\033[m'.format(valor))
print('o dobro desse numero é: \033[34m{}\033[m\no triplo desse numero é: \033[34m{}\033[m'.format(valor*2, valor*3))
print('a raiz quadrada dele será: \033[035m{:.2f}\033[m'.format(valor**(1/2)))
