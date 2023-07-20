'''Adapte o código do exercício 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.'''

import moeda

n = int(input('Digite um número: '))

print(f'O valor {moeda.moeda(n)} com um aumento de 10% é {moeda.moeda(moeda.aumentar(n,10))}.')
print(f'O valor {moeda.moeda(n)} com um desconto de 15% é {moeda.moeda(moeda.diminuir(n,15))}.')
print(f'O dobro do valor {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}.')
print(f'A metade do valor {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}.')