produtos = ('lapis', 1, 'borracha', 1.50, 'lapiseira', 3.20, 'grafite', 2, 'apontador', 2.50, 'caderno', 13.90)
print('='*35 + '\nLista de Compras\n' + '='*35)
for lista in range(0, len(produtos), 2):
    print(f'\033[33m{produtos[lista]:.<30}\033[mR$:{produtos[lista+1]}')
print('='*35)
