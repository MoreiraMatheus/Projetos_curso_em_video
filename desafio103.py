def ficha(nome='', gols=''):
    """
    Função que mostra uma pequena ficha sobre um jogador
    :param nome: Nome do jogador
    :param gols: Nº de gols
    :return: Nome + nº de gols
    """
    if nome == '':
        nome = '<desconhecido>'
    if gols not in '0123456789':
        gols = 0
    return print('='*40 + f'\nO jogador {nome} fez {gols} gol(s) no campeonato. ')


nomej = input('Nome do jogador: ').capitalize()
ngols = input('Nº de Gols: ')
ficha(nomej, ngols)
