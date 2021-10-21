num = []
maior = menor = 0
maiorp = menorp = ' '
for c in range(0, 5):
       num.append(int(input('Digite um numero: ')))
print(f'Você digitou os valores {num}')
for p, v in enumerate(num):
       if v == max(num):
              maior = v
              maiorp += str(p) + ' '
       elif v == min(num):
              menor = v
              menorp += str(p) + ' '
print(f'O maior valor foi {maior} nas posições {maiorp}')
print(f'O menor valor foi {menor} nas posições {menorp}')
