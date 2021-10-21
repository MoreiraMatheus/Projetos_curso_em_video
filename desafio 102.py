def fatorial(valor, show=False):
    """
    Função responsavel por mostrar o fatorial de um numero
    :param valor: Valor do fatorial
    :param show: Função que mostrará os calculos
    :return: resultado do fatorial e os calculos caso sejam exigidos
    """
    resultado = 1
    processo = ''
    for c in range(valor, 0, -1):
        resultado *= c
        if show:
            if c == 1:
                processo += str(c) + ' = '
            else:
                processo += str(c) + ' x '
    return print('='*30 + f'\nO fatorial de {valor} é \n{processo}{resultado}')


while True:
    fat = int(input('='*30 + '\nDeseja mostrar o fatorial de qual valor? '))
    calc = ' '
    while calc not in 'SN':
        calc = input('Deseja mostrar os calculos? [S/N]: ').strip().upper()[0]
        if calc not in 'SN':
            print('\033[31mDigite uma opção válida.\033[m')
    if calc == 'N':
        mostra = False
    else:
        mostra = True
    fatorial(fat, mostra)
    cont = ' '
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if cont not in 'SN':
            print('\033[31mDigite uma opção válida.\033[m')
    if cont == 'N':
        break
print('Fim do Programa.')
