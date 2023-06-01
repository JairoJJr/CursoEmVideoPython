'''Faça um programa que leia um ângulo qualquer e mostre na
 tela o valor do seno, cosseno e tangente desse ângulo.'''
 
from math import radians, sin, cos, tan
a = float(input('Digite uma ângulo qualquer: '))
sen = sin(radians(a))
cos = cos(radians(a))
tg = tan(radians(a))

print(f'O ângulo de {a} possui o seno de {sen:.2f}, o cosseno de {cos:.2f} e a tangente de {tg:.2f}.')
