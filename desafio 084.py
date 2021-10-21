maior = menor = 0
pessoas = list()
while True:
    pessoa = []
    pessoa.append(input('Nome: ').strip().capitalize())
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] < menor:
            menor = pessoa[1]
        if pessoa[1] > maior:
            maior = pessoa[1]
    pessoas.append(pessoa[:])
    cont = ' '
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if cont not in 'SN':
            print('\033[31mdigite uma opção valida.\033[m')
    if cont == 'N':
        break
print(f'você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}Kg que foi de ', end='')
for c in pessoas:
    if c[1] == maior:
        print(c[0], end=' ')
print(f'\nO menor peso foi de {menor}Kg que foi de ', end='')
for c in pessoas:
    if c[1] == menor:
        print(c[0], end=' ')
