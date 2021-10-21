import moeda

p = float(input('Digite um preço R$:'))
print('='*50)
print(f'A metade de {p} será {moeda.metade(p)}')
print(f'O dobro de {p} será {moeda.dobro(p)}')
print(f'Aumentando 10% de {p} será {moeda.aumentar(p, 10)}')
print(f'Diminuindo 15% de {p} será {moeda.diminuir(p, 15)}')
print('='*50)
