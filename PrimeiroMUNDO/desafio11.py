'''Faça um programa que leia a larguta e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pint-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

A = float(input('Qual a Altura da sua parede em metros:'))
B = float(input('Qual a Largura da sua parede em metros:'))
area = A * B
litro = area / 2

print('Sua parede possui {} metros quadrados, portanto para pintar sua parede você precisará de {:.2f} litros de tinta'.format(area, litro))

