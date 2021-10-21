def aumentar(n, porcento=0):
    p = porcento / 100
    n += n * p
    return n


def diminuir(n, porcento=0):
    p = porcento / 100
    n -= p * n
    return n


def dobro(n):
    n *= 2
    return n


def metade(n):
    n /= 2
    return n

