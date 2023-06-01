'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

num = int(input('Informe um número entre 0 e 9999: '))
u = num / 1 % 10
d = num / 10 % 10
c = num / 100 % 10
m = num / 1000 % 10

print(f'O número {int(num)} é formado por {int(u)} unidades, {int(d)} dezenas, {int(c)}'
      f' centenas e {int(m)} milhares.')