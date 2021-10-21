def voto(nasc):
    """
    Função que diz se a pessoa é obrigada a votar
    :param idade: ano de nascimento da pessoa
    :return: retorna uma mensagem dizendo
    se a pessoa é obrigada ou não a votar
    """
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos seu voto é Negado'
    elif idade in range(16, 18) or idade >= 65:
        return f'com {idade} anos seu voto é Opcional'
    else:
        return f'Com {idade} anos seu voto é Obrigatório'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
