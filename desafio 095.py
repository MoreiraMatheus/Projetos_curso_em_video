jogadores = list()
while True:
    jogador = dict()
    gols = list()
    total = 0
    jogador['nome'] = input('Nome do jogador: ').strip().capitalize()
    part = int(input('Quantas partidas o jogador jogou? '))
    for c in range(0, part):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = gols[:]
    for c in range(0, len(gols)):
        total += gols[c]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    cont = ' '
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if cont not in 'SN':
            print('\033[31mDigite uma opção válida.\033[m')
    if cont == 'N':
        break
print(jogadores)
print('='*45)
print(f'{"Nº":<5}"Gols"{"Total":>17}')
print('-'*45)
for n, j in enumerate(jogadores):
    print(f'\033[34m{n+1:<5}\033[m{j["gols"]}{j["total"]:>17}')
analise = ' '
while analise != 'exit':
    analise = input('Qual jogador deseja analisar?(\033[31m"exit"\033[m para sair) ')
    if analise == 'exit':
        print('\033[31mPrograma encerrado.\033[m')
    else:
        analise = int(analise) - 1
        print('=' * 45)
        print(f'O jogador {jogadores[analise]["nome"]} ', end='')
        print(f'jogou um total de {len(jogadores[analise]["gols"])} partidas.')
        for p, g in enumerate(jogadores[analise]["gols"]):
            print(f'Na {p + 1}ª partida fez {g} gols.')
        print(f'O total de gols foram {jogadores[analise]["total"]}')
        print('='*45)
