cont = 0
PA = 0

print('Gerador de PA\n', '='*10)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
while cont != 10:
    PA += r
    cont += 1
    print(PA, end=' ')
print('\nEsses são os 10 primeiros termos desta PA')
