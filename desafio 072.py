numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        resp = int(input('Diga um numero entre 0 e 20: '))
        if resp in range(0, 21):
            break
        print('\033[31mDigite uma opção valida\033[m')
    print(f'você digitou o numero \033[34m{numeros[resp]}\033[m')
    while True:
        cont = input('\nQuer continuar? [S/N]: ').strip().upper()[0]
        if cont in 'NS':
            break
        else:
            print('\033[31mDigite uma opção valida\033[m')
    if cont == 'N':
        break
print('Fim do programa')
