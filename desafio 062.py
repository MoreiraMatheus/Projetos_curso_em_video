mais = 1
cont = 10
PA = 0
term = 0

print('Gerador de PA\n', '='*10)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
while mais != 0:
    PA = pt
    while cont != 0:
        print(PA, end=' ')
        PA += r
        cont -= 1
        term += 1
    mais = int(input('\nDigite mais termos para que eu calcule: '))
    cont += mais
print('No total foram calculados \033[34m{}\033[m termos'.format(term))
