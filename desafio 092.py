from datetime import datetime
dados = dict()
dados['nome'] = input('Nome: ').strip().capitalize()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho ("0" caso não tenha): '))
if dados['ctps'] != 0:
    dados['contrat'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposent'] = (dados['contrat'] - nasc) + 35
print(f'Nome: \033[33m{dados["nome"]}\033[m')
print(f'Nascido em: \033[34m{nasc}\033[m//Idade: \033[34m{dados["idade"]}\033[m')
if dados['ctps'] != 0:
    print(f'Portador da carteira de Trabalho de numero: \033[34m{dados["ctps"]}\033[m')
    print(f'Contratado em \033[34m{dados["contrat"]}\033[m, com salário de \033[32m{dados["salario"]}R$\033[m')
    print(f'Irá se aposentar por volta dos \033[34m{dados["aposent"]}\033[m anos, ', end='')
    print(f'no ano de \033[34m{nasc + dados["aposent"]}\033[m')
