ano = int(input('me diga o ano em que você está: '))
etapa1 = ano % 4
etapa2 = ano % 100
etapa3 = ano % 400
if etapa1 == 0 and etapa2 != 0 or etapa3 == 0:
    print('é um ano bissexto.')
else:
    print('não é um ano bissexto.')
