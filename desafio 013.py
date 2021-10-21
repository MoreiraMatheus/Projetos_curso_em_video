salario = float(input('me diga seu salário: '))
aumento = salario * 0.15
print('seu salário é de \033[31m{}\033[m R$ com 15% de aumento será: '.format(salario), end=' ')
print('\033[31m{}\033[m R$'.format(salario + aumento))
