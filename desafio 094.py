pessoas = list()
idades = 0
while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ').strip().capitalize()
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
        if sexo not in 'MF':
            print('\033[31mDigite uma opção válida.\033[m')
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    idades += pessoa['idade']
    pessoas.append(pessoa.copy())
    cont = ' '
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if cont not in 'SN':
            print('\033[31mDigite uma opção válida.\033[m')
    if cont == 'N':
        break
media = idades / len(pessoas)
print(f'O total de pessoas cadastradas foi de {len(pessoas)}')
print(f'A média de idade do grupo é de {media:.2f}')
print('As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}]', end=' ')
print(f'\nAs pessoas acima da média de idade são ', end=' ')
for p in pessoas:
    if p['idade'] > media:
        print(p['nome'], end=' ')
