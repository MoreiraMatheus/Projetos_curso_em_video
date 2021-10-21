num = int(input('me diga um numero para virar fatorial: '))
control = num
fatorial = 1
while control > 0:
    fatorial *= control
    control -= 1
print('o fatorial de {} será {}'.format(num, fatorial))
