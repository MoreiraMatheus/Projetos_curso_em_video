def linha(txt, fcor=0):
    tam = len(txt) + 4
    print(f"\033[4{fcor}m{'=' * tam}\033[m")
    print(f'\033[4{fcor}m  {txt}  \033[m')
    print(f"\033[4{fcor}m{'=' * tam}\033[m")


def ajuda(func):
    print('\n\033[42m')
    help(func)
    print('\033[m')


while True:
    linha('Sistema de ajuda Programado', 3)
    comand = input('Função ou biblioteca ("FIM" para finalizar o programa): ').strip()
    if comand.upper() == 'FIM':
        linha('Encerrando programa', 1)
        break
    else:
        linha(f'Acessando o manual da função "{comand}', 4)
        ajuda(comand)
