from interface import *
from arquivo import *
from time import sleep
invalido = '\033[31mDigite uma opção válida.\033[m\n'
arq = 'Nomes_Cadastrados.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    opc = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if opc == 1:
        lerarquivo(arq)
        sleep(1)
    elif opc == 2:
        cab('Novo cadastro.')
        nome = input('Nome: ')
        idade = leiaint('idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)
    elif opc == 3:
        cab('Finalizando.')
        sleep(1)
        break
    else:
        print(invalido)
        sleep(1)
