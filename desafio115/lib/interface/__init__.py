def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite uma opção válida.\033[m')
            continue
        else:
            return num


def linha(tam=40):
    return '=' * tam


def cab(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cab('Menu')
    c = 1
    for itens in lista:
        print(f'\033[33m[ {c} ]\033[34m {itens}\033[m')
        c += 1
    print(linha())
    resp = leiaint('Sua escolha é: ')
    return resp
