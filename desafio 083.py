expressao = list(input('Digite uma expressão: '))
par = list()
valid = True
for c in expressao:
    if c == '(':
        par.append('(')
    elif c == ')':
        if len(par) > 0:
            par.pop()
        else:
            valid = False
            break
if valid:
    print('Sue expressão é valida.')
else:
    print('Sue expressão não é valida.')
