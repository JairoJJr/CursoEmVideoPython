'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações.'''

A = input('Digite qualquer coisa. ')

print(f'Só tem espaços: {A.isspace()}')
print(f'É um número: {A.isnumeric()}')
print(f'É alfabético: {A.isalpha()}')
print(f'É alfanumérico: {A.isalnum()}')
