'''Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos dólares ela pode contar.'''

R = float(input('Quantos Reais você tem na carteira?'))
D = R / 5
print('com R${:.2f} você compra U${:.2f} '.format(R,D))
