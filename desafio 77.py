palavras = ('Ovo', 'Aprender', 'Celular', 'Aprender')
print('O contador de Vogáis')
for p in palavras:
    print(f'\nNa palavra \033[33m{p}\033[m as vogais são ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
