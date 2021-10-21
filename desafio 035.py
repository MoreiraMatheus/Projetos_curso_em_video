r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))

if r1 < r2+r3 and r2 < r3+r1 and r3 < r1+r2:
    print('podem formar um triangulo')
else:
    print('não podem formar um triangulo')
