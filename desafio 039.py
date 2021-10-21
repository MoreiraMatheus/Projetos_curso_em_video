from datetime import date
ano = int(input('me diga seu ano de nascimento: '))
data = date.today().year
idade = data - ano
print('quem nasceu em \033[33m{}\033[m possui \033[33m{}\033[m anos'.format(ano, idade))
if idade < 18:
    print('voce ainda \033[31mnão\033[m precisa se alistar, faltam \033[33m{}\033[m anos'.format(18-idade))
elif idade == 18:
    print('você está na idade de se alistar')
else:
    print('você já deveria ter se alistado a \033[33m{}\033[m anos atrás'.format(idade-18))
