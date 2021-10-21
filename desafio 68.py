from random import randint

win = cont = result = 0
invalido = '\033[31mDigite uma opção valida.\033[m'

print('Vamos Jogar par ou Impar')
while True:
    pc = randint(1, 11)
    pi = input('Par ou Impar[P/I]: ').strip().upper()[0]
    if pi == 'P' or pi == 'I':
        player = int(input('Diga um valor: '))
        cont += 1
        result = (pc + player) % 2
        if pi == 'P':
            if result == 0:
                print(f'Você jogou {player} e o computador jogou {pc}.')
                print('\033[32mVitoria\033[m')
                win += 1
            else:
                print(f'Você jogou {player} e o computador jogou {pc}.')
                print('\033[31mDerrota\033[m')
                break
        elif pi == 'I':
            if result == 1:
                print(f'Você jogou {player} e o computador jogou {pc}.')
                print('\033[32mVitoria\033[m')
                win += 1
            else:
                print(f'Você jogou {player} e o computador jogou {pc}.')
                print('\033[31mDerrota\033[m')
                break
    else:
        print(invalido)
print(f'Você jogou um total de \033[34m{cont}\033[m partidas e obteve \033[34m{win}\033[m vitórias.')
