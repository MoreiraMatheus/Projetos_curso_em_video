# quantas vezes aparece o valor 9, em que posição foi digitado o primeiro 3, quais foram os numeros pares
numeros = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
           int(input('Digite um numero: ')), int(input('Digite um numero: ')))
if numeros.count(9) != 0:
    print(f'O numero 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro numero 3 foi digitado na {numeros.index(3)+1} casa')
print('os numeros pares digitados foram:', end=' ')
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=' ')
