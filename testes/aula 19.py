lista = []
print(f'{" Listinha de animes ":=^40}')
while True:
    anime = dict()
    anime['nome'] = input('Nome: ').strip().capitalize()
    estado = ' '
    while estado not in 'CA':
        estado = input('Concluido ou Assistindo?: ').strip().upper()[0]
        anime['estado'] = estado
        if estado not in 'CA':
            print('\033[31mDigite uma opção válida.\033[m')
    lista.append(anime)
    print(lista)
