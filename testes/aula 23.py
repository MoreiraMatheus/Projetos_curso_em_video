try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro numero: '))
except Exception as error:
    print(error.__class__)
else:
    print(f'A soma de {n1}+{n2} é {n1 + n2}')
finally:
    print('Volte sempre.')
