num1 = int(input('me diga um numero inteiro: '))
num2 = int(input('me diga outro numero inteiro: '))
if num1 > num2:
    print('o \033[31mprimeiro\033[m valor é maior que o \033[32msegundo\033[m')
elif num1 < num2:
    print('o \033[32msegundo\033[m valor é maior que o \033[31mprimeiro\033[m')
else:
    print('ambos os numeros são \033[33miguais\033[m')
print('-='*3, 'fim do programa', '=-'*3)
