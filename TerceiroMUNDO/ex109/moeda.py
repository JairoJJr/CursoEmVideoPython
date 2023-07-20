def aumentar(num=0, p=0, m=False):
    aumento = num + (num*p/100)
    return aumento if m is False else moeda(aumento)


def diminuir(num=0 , p=0, m=False):
    dimin = num + (num*p/100)
    return dimin if m is False else moeda(dimin)


def dobro(num=0, m=False):
    d = num*2
    return d if m is False else moeda(d)


def metade(num=0, m=False):
    med = num / 2
    return med if m is False else moeda(med)


def moeda(preço=0, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace('.' , ',')

