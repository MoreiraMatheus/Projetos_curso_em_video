valor = int(input('me diga um numero inteiro: '))
print('você escolheu o numero: \033[1;32m{}\033[m'.format(valor))
print('seu antecesor serà: \033[36m{}\033[m \nseu sucessor será: \033[36m{}\033[m'.format(valor - 1, valor + 1))
