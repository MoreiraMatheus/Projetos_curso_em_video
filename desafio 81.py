valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    cont = ' '
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N]: ').upper().strip()[0]
        if cont != 'N' and cont != 'S':
            print('Opção invalida')
    if cont == 'N':
        break
print(f'Você digitou {len(valores)} numeros.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente serão {valores}')
if 5 in valores:
    print('O 5 está entre os numeros digitados')
