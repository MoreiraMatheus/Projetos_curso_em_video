num = int(input('me diga um numero inteiro: '))
esc = int(input('''Escolha uma das opções abaixo:
[1] \033[32mBinário\033[m
[2] \033[34mOctal\033[m
[3] \033[31mHexadecimal\033[m
'''))
if esc == 1:
    print('O numero {} em binário será {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('O numero {} em Octal será {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('o numero {} em Hexadecimal será {}'.format(num, hex(num)[2:]))
