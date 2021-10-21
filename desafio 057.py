n = 1
msg = ''
while n == 1:
    sexo = input('me diga seu sexo[M/F]: ').upper().strip()
    if sexo == 'M':
        msg = '\033[34mMasculino\033[m'
        n = 0
    elif sexo == 'F':
        n = 0
        msg = '\033[35mFeminino\033[m'
    else:
        print('não entendi, por favor digite uma opção válida')
        n = 1
print('entendi então você é do sexo {}'.format(msg))
