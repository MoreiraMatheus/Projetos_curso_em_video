import random

# coletando os nomes dos alunos
a1 = input('me diga o nome de um aluno: ')
a2 = input('me diga o nome de outro: ')
a3 = input('me diga o nome de mais um: ')
a4 = input('me diga o nome de um ultimo aluno:')
lista = [a1, a2, a3, a4]

# escolhendo a ordem
random.shuffle(lista)
print(lista)
