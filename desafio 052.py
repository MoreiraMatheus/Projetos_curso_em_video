num = int(input('me diga um numero: '))
div = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m', end='')
        div += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[m\no numero {} foi dividido {} vezes, portanto'.format(num, div))
if div == 2:
    print('É um numero primo')
else:
    print('Não é um numero primo')
