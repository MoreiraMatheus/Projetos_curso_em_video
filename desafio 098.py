from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print('=' * 40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        fim2 = fim - 1
        passo *= -1
        for c in range(inicio, fim2, passo):
            print(c, end=' ')
            sleep(0.3)
    else:
        fim2 = fim + 1
        for c in range(inicio, fim2, passo):
            print(c, end=' ')
            sleep(0.3)
    print()


contador(1, 10, 1)
contador(10, 0, -2)
contador(int(input('Inicio: ')),
         int(input('Fim:    ')),
         int(input('Passo:  ')))
