maior = H = menos20 = 0
invalido = '\033[31mDigite uma opção válida.\033[m\n'

print('O cadastrador de Pessoas 2000kkkk')
while True:
    print('-'*30 + '\nCadastre uma pessoa\n' + '-'*30)
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    retorno = False
    while not retorno:
        sexo = input('Sexo[M/F]:').upper().strip()[0]
        if sexo == 'M' or sexo == 'F':
            if sexo == 'M':
                H += 1
            elif sexo == 'F' and idade < 20:
                menos20 += 1
            retorno = True
        else:
            print(invalido)
    cont = ' '
    while cont not in 'SN':
        cont = input('Deseja continuar?[S/N] ').upper().strip()[0]
    if cont == 'N':
        break
print(f'De todas as pessoas cadastradas {H} são homens, {maior} são de maior e {menos20} são mulheres com menos de 20')
