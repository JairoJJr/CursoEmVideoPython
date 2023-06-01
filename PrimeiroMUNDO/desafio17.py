'''Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo. Calcule e mostre o comprimento
da hipotenusa.'''

'''from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = sqrt(co**2 + ca**2)


print(f'O valor da hipotenusa é {h:.2f}')'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(co,ca)

print(f'O valor da hipotenusa é {h:.2f}')
