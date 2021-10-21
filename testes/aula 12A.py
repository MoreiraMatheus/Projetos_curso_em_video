nome = input('qual é seu nome? ')
nome = nome.lower()
if nome == 'matheus':
    print('\033[32mgostei muito do seu nome:)\033[m')
elif nome == 'pedro':
    print('\033[31mGRRRR PEDRO\033[m')
else:
    print('hmmm legal sue nome')
nome = nome.title()
print('bom dia \033[34m{}\033[m'.format(nome))
