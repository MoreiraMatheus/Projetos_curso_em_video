cidade = input('me diga o nome de uma cidade: ')
cidade = cidade.strip()
cidade = cidade.lower()
nome = cidade.split()
if 'santo' in nome[0]:
    print('sua cidade começa com santo')

else:
    print('sua cidade não começa com santo')
