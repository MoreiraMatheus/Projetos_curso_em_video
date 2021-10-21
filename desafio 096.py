def area(larg, comp):
    a = larg * comp
    print(f'A area do terreno \033[34m{larg:.2f}\033[m x \033[34m{comp:.2f}\033[m é de \033[34m{a:.2f}\033[mm²')


area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
