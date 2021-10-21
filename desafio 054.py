from datetime import date

maior = 0
menor = 0

quant = int(input('me diga um numero de pessoas: '))
for pessoa in range(1, quant + 1):
    ano = int(input('me diga em que ano a {} pessoa nasceu: '.format(pessoa)))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Das \033[34m{}\033[m pessoas analisadas, \033[33m{}\033[m '.format(quant, maior), end='')
print('são de maior e \033[33m{}\033[m são de menor'.format(menor))
