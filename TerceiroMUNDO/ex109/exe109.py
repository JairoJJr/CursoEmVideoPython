'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.'''

import moeda

n = int(input('Digite um número: '))

print(f'O valor {moeda.moeda(n)} com um aumento de 10% é {moeda.aumentar(n,10,True)}.')
print(f'O valor {moeda.moeda(n)} com um desconto de 15% é {moeda.diminuir(n,15,True)}.')
print(f'O dobro do valor {moeda.moeda(n)} é {moeda.dobro(n,True)}.')
print(f'A metade do valor {moeda.moeda(n)} é {moeda.metade(n,True)}.')