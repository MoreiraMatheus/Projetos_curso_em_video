frase = input('me diga uma frase: ').strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for posi in range(len(junto) - 1, -1, -1):
    inverso += junto[posi]
print('Sua frase foi \033[34m{}\033[m\nSua frase ao contrário fica \033[34m{}\033[m'.format(junto, inverso))
if inverso == junto:
    print('A frase é um palindromo')
else:
    print('A frase \033[31mnão\033[m é um palindromo')
