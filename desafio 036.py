casa = float(input('me diga o valor da casa: '))
salario = float(input('me diga seu salário: '))
anos = int(input('me diga em quantos anos você pretende pagar a casa: '))
prest = casa/(anos*12)
print('o valor da casa será: \033[32mR${:.2f}\033[m, em parcelas de'.format(casa), end=' ')
print('\033[32mR${:.2f}\033[m por mês a cada \033[34m{}\033[m anos'.format(prest, anos))
if salario * 0.3 >= prest:
    print('emprestimo \033[32mAPROVADO\033[m!')
else:
    print('emprestimo \033[31mNEGADO\033[m!')
