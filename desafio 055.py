menor = 0
maior = 0

quant = int(input('me diga quantas pessoas deseja analisar: '))
for pessoa in range(1, quant + 1):
    peso = float(input('qual o peso da {} pessoa? '.format(pessoa)))
    if pessoa == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O menor peso analisado foi \033[34m{}\033[mKg'.format(menor))
print('O maior peso analisado foi \033[34m{}\033[mKg'.format(maior))
