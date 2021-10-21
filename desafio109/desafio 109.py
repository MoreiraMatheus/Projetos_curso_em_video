import moeda

p = float(input('Digite um preço R$:'))
print('='*50)
print(f'A metade de {moeda.moeda(p)} será {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} será {moeda.dobro(p, True)}')
print(f'Aumentando 10% de {moeda.moeda(p)} será {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 15% de {moeda.moeda(p)} será {moeda.diminuir(p, 15, True)}')
print('='*50)
