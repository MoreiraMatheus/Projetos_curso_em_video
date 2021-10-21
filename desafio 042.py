print('me diga três retas e eu direi se elas podem ou não formar um triângulo')
r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))

if r1 < r2+r3 and r2 < r3+r1 and r3 < r1+r2:
    if r1 == r2 == r3:
        tri = '\033[31mEquilatero\033[m'
    elif r1 == r2 or r2 == r3 or r3 == r1:
        tri = '\033[33mIsóceles\033[m'
    else:
        tri = '\033[34mEscaleno\033[m'
    print('essas 3 retas podem formar um triangulo do tipo {}'.format(tri))
    if r1 == r2 == r3 == 7:
        print('TRIANGULO RAFA MOREIRA MANO 777 KKKKKJ')
else:
    print('não podem formar um triangulo')
