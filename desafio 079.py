valores = list()
while True:
    add = int(input('Diga um valor: '))
    if add not in valores:
        valores.append(add)
        cont = ' '
        while cont not in 'SN':
            cont = input('Deseja continuar? [S/N]: ').upper().strip()[0]
            if cont != 'N' and cont != 'S':
                print('Opção invalida')
        if cont == 'N':
            break
    else:
        print('Esse valor já está na lista')
print(f'Os valores digitados foram {sorted(valores)}')
