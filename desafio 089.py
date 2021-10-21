alunos = list()
while True:
    nome = input('Nome: ').strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    cont = ' '
    while cont not in 'NS':
        cont = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if cont not in 'NS':
            print('\033[31mDigite uma opção válida.\033[m')
    if cont == 'N':
        break
print(f'{"Boletim":=^40}')
for p in range(0, len(alunos)):
    print(f'nº: \033[34m{p+1}\033[m Nome: \033[34m{alunos[p][0]}\033[m média: \033[34m{alunos[p][2]}\033[m')
print('='*40)
atv = ' '
while atv != 'exit':
    atv = input('Mostrar notas de qual aluno? ("\033[31mexit\033[m" para sair): ')
    if atv != 'exit':
        print(f'As notas de {alunos[int(atv)-1][0]} foram:', end='')
        for c in alunos[int(atv)-1][1]:
            print(f'{c} ', end='')
        print()
    print('='*40)
