def aumentar(num=0, p=0):
    aumento = num + (num*p/100)
    return aumento


def diminuir(num=0 , p=0):
    dimin = num + (num*p/100)
    return dimin


def dobro(num=0):
    d = num*2
    return d


def metade(num=0):
    m = num / 2
    return m


def moeda(preço=0, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace('.' , ',')
