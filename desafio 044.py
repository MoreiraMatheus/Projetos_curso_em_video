print('==='*3, 'lojinha', '==='*3)
valor = float(input('Valor das compras: R$'))
final = valor
pag = int(input('''Sua forma de pagamento será:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão
'''))
if pag == 1:
    final = valor - (valor * 0.1)
elif pag == 2:
    final = valor - (valor * 0.05)
elif pag == 3:
    final = valor
    print('sua compra terá o valor de \033[32m{}\033[m parcelado em \033[34m2x\033[m'.format(valor))
elif pag == 4:
    parc = int(input('em quantas parcelas você deseja pagar?'))
    final = valor + (valor * 0.2)
    print('sua compra terá o valor de \033[32m{}\033[m parcelado em \033[34m{}x\033[m'.format(final, parc))
print('sua compra de \033[32mR${}\033[m terá o valor final de \033[32m{}\033[m'.format(valor, final))
