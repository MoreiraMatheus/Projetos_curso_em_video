valor = 0
while True:
    valor = int(input('Diga um valor para ver a tabuada do mesmo: '))
    if valor < 0:
        break
    print('='*30)
    for x in range(1, 11):
        print(f'{valor} x {x} = {valor*x}')
    print('=' * 30)
print('Programa encerrado.')
