cinquenta = vinte = dez = um = 0
print('-'*40, '\nCaixa eletrônico programado\n' + '-'*40)
saque = int(input('Qual valor você deseja sacar? R$: '))
while True:
    if saque - 50 >= 0:
        saque -= 50
        cinquenta += 1
    elif saque - 20 >= 0:
        saque -= 20
        vinte += 1
    elif saque - 10 >= 0:
        saque -= 10
        dez += 1
    elif saque - 1 >= 0:
        saque -= 1
        um += 1
    else:
        break
if cinquenta >= 1:
    print(f'{cinquenta} Notas de 50R$')
if vinte >= 1:
    print(f'{vinte} Notas de 20R$')
if dez >= 1:
    print(f'{dez} Notas de 10R$')
if um >= 1:
    print(f'{um} Notas de 1R$')
