num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um numero: ')))
    cont = ' '
    while cont not in 'sn':
        cont = input('Deseja continuar? [S/N]: ').lower().strip()[0]
        if cont != 's' and cont != 'n':
            print('Opção invalida.')
    if cont == 'n':
        break
for pos in range(0, len(num)):
    if num[pos] % 2 == 0:
        pares.append(num[pos])
    elif num[pos] % 2 == 1:
        impares.append(num[pos])
print(f'Os numeros que você digitou foram {num}')
print(f'Dentre eles os pares são {pares}')
print(f'Dentre eles os impares são {impares}')
