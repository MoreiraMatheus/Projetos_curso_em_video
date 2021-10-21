aluno = dict()
aluno['Nome'] = input('Nome: ').strip().capitalize()
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 5:
    aluno['Situação'] = '\033[32mAprovado.\033[m'
else:
    aluno['Situação'] = '\033[31mReprovado.\033[m'
print('='*30)
for k, v in aluno.items():
    print(f'{k} = {v}')
print('='*30)
