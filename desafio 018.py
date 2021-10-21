import math

angulo = float(input('me diga um valor de um ângulo: '))
angulo = math.radians(angulo)

# seno:
print('o seno desse ângulo será: {:.2f} '.format(math.sin(angulo)))

# cosseno:
print('o cosseno desse ângulo será: {:.2f}'.format(math.cos(angulo)))

# tangente:
print('a tangente desse ânglo será: {:.2f}'.format(math.tan(angulo)))
