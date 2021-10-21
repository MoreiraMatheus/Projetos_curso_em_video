dist = float(input('me diga a distância da sua viagem'))
if dist <= 200:
    valor = dist * 0.5
    print('o valor da sua viagem será: {:.2f}R$'.format(valor))
else:
    valor = dist * 0.45
    print('o valor da sua viagem será: {:.2f}R$'.format(valor))
