from desafio107 import moeda


def leiadin(txt):
    valor = input(txt).strip()
    if valor == '':
        valor = 'a'
    while valor not in '0123456789':
        print('\033[31mDigite uma opção válida.\033[m')
        valor = input(txt)
        if valor == '':
            valor = 'a'
    int(valor)
    return valor


num = leiadin('Digite um valor: ')
moeda.resumo(num, 10, 15, True)
