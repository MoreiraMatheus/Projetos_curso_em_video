base = float(input('me diga a largura de uma parede: '))
altura = float(input('me diga a altura da mesma parede: '))
area = base * altura
print('a area da sua parede é de \033[31m{}\033[m m^2. '.format(area))
print('para pintar ela será necessário: \033[31m{}\033[m litros de tinta'.format(area/2))
