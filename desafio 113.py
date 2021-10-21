def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite uma opção válida.\033[m')
            continue
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite uma opção válida.\033[m')
        else:
            return num


inteiro = leiaint('Digite um inteiro: ')
real = leiafloat('Digite um real: ')
print(f'O numero inteiro digitado foi {inteiro}.\nO numero real digitado foi {real}.')
