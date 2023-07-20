'''Crie um modulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''


from ex107 import moeda

n = int(input('Digite um número: '))

print(f'O valor {n} com um aumento de 10% é {moeda.aumentar(n,10)}.')
print(f'O valor {n} com um desconto de 15% é {moeda.diminuir(n,15)}.')
print(f'O dobro do valor {n} é {moeda.dobro(n)}.')
print(f'A metade do valor {n} é {moeda.metade(n)}.')