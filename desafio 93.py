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
print('='*45)
print(f'O jogador {jogador["nome"]} jogou um total de {len(jogador["gols"])} partidas.')
for p, g in enumerate(gols):
    print(f'Na {p+1}ª partida fez {g} gols.')
print(f'O total de gols foram {total}')
print('='*45)
