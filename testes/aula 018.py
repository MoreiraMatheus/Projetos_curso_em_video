pessoas = list()
while True:
    dados = list()
    nome = input('Diga o nome para cadastrar: ')
    idade = int(input('Diga a idade para cadastrar: '))
    dados.append(nome)
    dados.append(idade)
    pessoas.append(dados)
    print('\nas pessoas cadastradas até o momento foram:')
    for p in pessoas:
        print(f'{p[0]} com {p[1]} anos.')
