import math

cateto1 = float(input('me diga um valor para um cateto: '))
cateto2 = float(input('me diga um valor para outro cateto'))
print('o valor da hipotenusa dos dois catetos será:', end=' ')
print('{:.2f}'.format(math.hypot(cateto1, cateto2)))
