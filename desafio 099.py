from random import randint

quant = randint(0, 10)
valores = list()


def maior(num):
    print('=' * 70)
    if len(num) == 0:
        print('Não recebi nenhum valor, não há o que eu possa fazer.')
    else:
        print(f'Recebi {len(num)} valores, sendo eles {sorted(num)}, o maior de todos foi {max(num)}')
    print('='*70)


for c in range(0, quant):
    valores.append(randint(1, 10))
maior(valores)
