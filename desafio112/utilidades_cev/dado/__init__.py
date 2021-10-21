def leiadin(txt):
    valido = False
    while not valido:
        valor = input(txt).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            print('\033[31mDigite uma opção válida.\033[m')
        else:
            valido = True
            return float(valor)
