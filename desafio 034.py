salario = float(input('me diga seu salário: '))
if salario <= 1250:
    aumento = salario * 0.15
    print('seu salário é de {} com um aumento de 15% será de {}'.format(salario, salario + aumento))
else:
    aumento = salario * 0.1
    print('seu salário é de {} com um aumento de 15% será de {}'.format(salario, salario + aumento))
