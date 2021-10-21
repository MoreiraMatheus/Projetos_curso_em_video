def moeda(v):
    v = f'\033[32mR${v:.2f}\033[m'.replace('.', ',')
    return v


def aumentar(n=0, porcento=0, form=False):
    p = porcento / 100
    n += n * p
    if form:
        n = moeda(n)
    return n


def diminuir(n=0, porcento=0, form=False):
    p = porcento / 100
    n -= p * n
    if form:
        n = moeda(n)
    return n


def dobro(n=0, form=False):
    n *= 2
    if form:
        n = moeda(n)
    return n


def metade(n=0, form=False):
    n /= 2
    if form:
        n = moeda(n)
    return n
