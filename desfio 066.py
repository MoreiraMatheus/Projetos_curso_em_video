soma = cont = 0
while True:
    n = int(input('Digite um numero [\033[34m999\033[m para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou \033[34m{cont}\033[m numeros e a soma de todos eles é \033[33m{soma}\033[m.')
