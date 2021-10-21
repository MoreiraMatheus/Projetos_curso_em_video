n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
menu = 0
while menu != 5:
    menu = int(input('''\ncerto agora escolha o que você deseja fazer com esses dois numeros
\033[33m[ 1 ]\033[34m Soma\033[m
\033[33m[ 2 ]\033[34m Multiplicação\033[m
\033[33m[ 3 ]\033[34m Descobrir qual o maior\033[m
\033[33m[ 4 ]\033[34m Adicionar novos numeros\033[m
\033[33m[ 5 ]\033[34m Sair do programa\033[m
sua escolha é: '''))
    if menu == 1:
        print('a soma de \033[34m{}\033[m e \033[34m{}\033[m é \033[34m{}\033[m'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('\033[34m{}\033[m multiplicado por \033[34m{}\033[m será \033[34m{}\033[m'.format(n1, n2, n1*n2))
    elif menu == 3:
        if n1 > n2:
            print('\033[34m{}\033[m é maior que \033[34m{}\033[m'.format(n1, n2))
        else:
            print('\033[34m{}\033[m é maior que \033[34m{}\033[m'.format(n2, n1))
    elif menu == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif menu == 5:
        print('finalizando...')
    else:
        print('\033[31mopção inválida\033[m')
