s = 0
cont = 0
print('\033[31meu somarei numeros pares para você\033[m')
for c in range(1, 7):
    valor = int(input('me diga o {} valor: '.format(c)))
    if valor % 2 ==0:
        s += valor
        cont += 1
print('você me disse {} numeros pares e a soma deles é {}'.format(cont, s))
