def leiaint(num):
    if num == '':
        num = 'a'
    while num not in '0123456789':
        print('\033[31mDigite uma opção válida.\033[m')
        num = input('Digite um numero: ').strip()
        if num == '':
            num = 'a'
    return num


n = leiaint(input('Digite um número: ').strip())
print('='*30 + f'\nVocê digitou o número \033[34m{n}\033[m')
