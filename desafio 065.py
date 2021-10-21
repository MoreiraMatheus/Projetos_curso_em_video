quant = num = cont = soma = maior = menor = med = 0

while cont != 'N':
    num = int(input('Diga um numero: '))
    quant += 1
    if maior == 0 and menor == 0:
        maior = menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
    cont = input('Deseja continuar? [S/N]: ').strip().upper()
    soma += num
print('''Você digitou \033[34m{}\033[m numeros
A média desses valores é \033[34m{}\033[m
Maior: \033[31m{}\033[m // Menor: \033[33m{}\033[m'''.format(quant, soma/quant, maior, menor))
