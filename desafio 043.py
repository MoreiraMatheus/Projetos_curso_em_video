peso = float(input('me diga seu peso(Kg): '))
alt = float(input('me diga sua altura(M): '))
imc = peso / (alt ** 2)
print('seu IMC é de {:.2f} portanto você está'.format(imc), end=' ')
if imc < 18.5:
    print('\033[31mabaixo do peso\033[m')
elif 18.5 <= imc < 25:
    print('no \033[32mpeso ideal\033[m')
elif 25 <= imc < 30:
    print('em \033[31msobrepeso\033[m')
elif 30 <= imc < 40:
    print('na faixa de \033[31mobesidade\033[m')
elif imc > 40:
    print('na faixa de \033[31mobesidade morbida\033[m, cuidado')
