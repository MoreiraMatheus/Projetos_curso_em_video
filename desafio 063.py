t1 = 0
t2 = 1
result = 0
cont = 3

print('-'*30 + '\nSequencia de Fibonacci\n' + '-'*30)
n = int(input('Quantos termos você deseja ver: '))
print(t1, t2, end=' ')
while cont <= n:
    result = t1 + t2
    print(result, end=' ')
    t1 = t2
    t2 = result
    cont += 1
print('\nFIM')
