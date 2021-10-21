import random

# coletando os nomes dos alunos
aluno1 = input('me diga o nome de um aluno: ')
aluno2 = input('me diga o nome de outro: ')
aluno3 = input('me diga o nome de mais um: ')
aluno4 = input('me diga o nome de um ultimo aluno:')
lista = [aluno1, aluno2, aluno3, aluno4]

# escolhendo o aluno
escolha = random.choice(lista)

print('o sistema escolheu o aluno: {}'.format(escolha))
