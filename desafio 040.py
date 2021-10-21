n1 = float(input('nota1: '))
n2 = float(input('nota2: '))
media = (n1+n2)/2
if media < 5.0:
    print('o aluno foi \033[31mREPROVADO\033[m!')
elif media < 6.9 and media >= 5.0:
    print('o aluno está de \033[34mRECUPERAÇÃO\033[m')
else:
    print('o aluno foi \033[32mAPROVADO\033[m!')
