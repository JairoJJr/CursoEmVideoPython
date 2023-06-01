'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

p1 = float(input('Preço do produto '))
p2 = p1 - p1 * 0.05
print('O valor do seu produto com desconto de 5% é R${:.2f}.'.format(p2))  