v1 = int(input('primeiro valor: '))
v2 = int(input('segundo valor: '))
v3 = int(input('terceiro valor: '))
maior = 0
menor = 0

if v1 > v2 and v1 > v3:
    maior = v1
elif v2 > v1 and v2 > v3:
    maior = v2
elif v3 > v1 and v3 > v2:
    maior = v3

if v1 < v2 and v1 < v3:
    menor = v1
elif v2 < v1 and v2 < v3:
    menor = v2
elif v3 < v1 and v3 < v2:
    menor = v3

print('o maior valor é: {}\no menor valor é: {}'.format(maior, menor))
