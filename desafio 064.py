soma = cont = 0
num = int(input('Me diga um numero inteiro [999 para parar o programa]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Me diga um numero inteiro [999 para parar o programa]: '))
print('Você digitou {} numeros a soma deles é {}'.format(cont, soma))
