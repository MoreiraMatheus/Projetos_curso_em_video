preço = float(input('me diga o preço de um produto: '))
desc = int(input('me diga uma porcentagem para desconto: '))
desc = desc / 100
print('seu produto com \033[7;40m{}%\033[m de desconto terá o valor de \033[1;32m{}\033[m'.format(desc * 100, preço - preço * desc))
