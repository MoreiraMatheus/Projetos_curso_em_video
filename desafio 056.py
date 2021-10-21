media = 0
hnome = ''
hvelho = 0
menos20 = 0
countH = 0
countM = 0

quant = int(input('me diga quantas pessoas você deseja analisar: '))
print('preencha os seguintes dados:')
for p in range(1, quant + 1):
    print('-'*5, '{}ª pessoa'.format(p), '-'*5)
    nome = input('Nome: ').strip().capitalize()
    sexo = input('Sexo [H/M]: ').strip().upper()
    idade = int(input('idade: '))
    media += idade
    if p == 1 and sexo == 'H':
        hnome = nome
        hvelho = idade
    elif sexo == 'H':
        countH += 1
        if idade > hvelho:
            hvelho = idade
            hnome = nome
    elif sexo == 'M':
        countM += 1
        if idade < 20:
            menos20 += 1

print('A média de idade dessas pessoas é de {:.2f} anos'.format(media/quant))
if countH != 0:
    print('O homem mais velho possui {} anos e se chama {}'.format(hvelho, hnome))
elif countM != 0:
    print('{} mulheres possuem menos de 20 anos'.format(menos20))
