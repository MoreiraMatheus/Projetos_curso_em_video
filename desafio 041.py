from datetime import date
ano = int(input('me diga o ano do seu nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('você possui \033[33m{}\033[m anos e esta na categoria \033[34mMirim\033[m'.format(idade))
elif idade <= 14 and idade >= 10:
    print('você possui \033[33m{}\033[m anos e está na categoria \033[34mInfantil\033[m'.format(idade))
elif idade <= 19 and idade >= 15:
    print('você possui \033[33m{}\033[m anos e está na categoria \033[34mJunior\033[m'.format(idade))
elif idade == 20:
    print('você possui \033[33m20\033[m anos e está na categoria \033[34mSênior\033[m')
else:
    print('você possui \033[33m{}\033[m anos e está na categoria \033[34mMaster\033[m'.format(idade))
print('\033[46mBoa competição\033[m')
