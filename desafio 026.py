frase = input('me diga uma frase: ')
frase = frase.strip().lower()
print('na sua frase a letra "A" aparece {} vezes'.format(frase.count('a')))
print('ela aparece pela primeira vez no {} caractere'.format(frase.find('a')))
print('e pela ultima no carcatere {}'.format(frase.rfind('a')))
