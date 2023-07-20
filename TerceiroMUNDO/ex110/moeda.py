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
    met = num / 2
    return met if m is False else moeda(met)


def moeda(preço=0, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace('.' , ',')

def resumo(num=0, aum=0, dim=0):
    aumento = aumentar(num, aum, True)
    dimin = diminuir(num, dim, True)
    d = dobro(num,True)
    met = metade(num, True)
    print('=-'*20)
    print('Resumo do Valor'.center(40))
    print('=-'*20)
    print(f'Preço analisado: \t\t{moeda(num)}')
    print(f'Dobro do preço: \t\t{d}')
    print(f'Metade do preço: \t\t{met}')
    print(f'{aum}% de aumento: \t\t{aumento}')
    print(f'{dim}% de redução: \t\t{dimin}')
    print('=-'*20)