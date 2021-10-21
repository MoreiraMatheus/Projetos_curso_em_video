import moeda

p = float(input('Digite um preço R$:'))
print('='*50)
print(f'A metade de {moeda.moeda(p)} será {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} será {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)} será {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 15% de {moeda.moeda(p)} será {moeda.moeda(moeda.diminuir(p, 15))}')
print('='*50)
