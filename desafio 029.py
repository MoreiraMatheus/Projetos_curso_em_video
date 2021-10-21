velo = float(input('me diga a velocidade do seu carro: '))
if velo <= 80:
    print('compreensivel tenha um ótimo dia')
else:
    multa = velo - 80
    multa = multa*7
    print('você ultrapassou o limite de velocidade de 80Km/h portanto será multado')
    print('valor da multa: {:.2f}R$'.format(multa))
