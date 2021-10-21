maismil = total = barato = nbarato = 0
print('='*30 + '\n\033[33mLista de compras\033[m\n' + '='*30)
while True:
    nome = input('Produto: ')
    preco = float(input('Preço: '))
    # Soma o total gasto
    total += preco
    # descobre quantos produtos valem mais de mil reais
    if preco > 1000:
        maismil += 1
    # Descobre o produto mais barato e seu preço
    if barato == 0 or barato > preco:
        barato = preco
        nbarato = nome
    cont = ' '
    while cont not in 'SN':
        cont = input('Deseja continuar[S/N]? ').strip().upper()[0]
        if cont != 'N' or cont != 'S':
            print('\033[31mDigite uma opção válida.\033[m')
    if cont == 'N':
        break
print(f'O total gasto foi: \033[32m{total} R$\033[m.')
print(f'\033[34m{maismil}\033[m produtos valem mais de mil reais.')
print(f'O produto mais barato foi \033[34m{nbarato}\033[m custando \033[32m{barato} R$\033[m')
