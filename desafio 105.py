def notas(*notas, sit=False):
    """
    ->ficha de uma sala de aula
    :param notas: notas dos alunos (aceita várias)
    :param sit: situação da sala (opcional)
    :return: dicionários com todas as informações
    """
    info = dict()
    info['quant'] = len(notas)
    info['maior'] = max(notas)
    info['menor'] = min(notas)
    med = sum(notas) / len(notas)
    info['media'] = med
    if sit:
        if med >= 7:
            info['sit'] = 'Boa'
        elif 5 < med < 7:
            info['sit'] = 'Razoavel'
        else:
            info['sit'] = 'Ruim'
    return info


print('='*40)
result = notas(10, 6, 8, 5, sit=True)
for k, v in result.items():
    print(f'\033[34m{k}\033[m = \033[33m{v}\033[m')
help(notas)
