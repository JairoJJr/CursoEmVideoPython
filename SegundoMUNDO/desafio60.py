'''Faça um programa que leia um número qualquer e mostre seu fatorial.
Use FOR e WHILE.'''

num = int(input('Digite um número inteiro qualquer: '))

print('=-=-=Resultado usando FOR:=-=-= ')
f = 1
for c in range(num,0,-1):
    print(c, end = ' ')
    if c != 1:
        f *= (c)
print(f'''
O fatorial de {num} é igual a {f}.''')

print('=-=-=Resultado usando o WHILE:=-=-=')

ct = num
ff = 1
while ct > 0:
    print(ct, end = ' ')
    print(' x ' if ct > 1 else " = ", end = ' ')
    ff *= ct
    ct -= 1
print(f'''{ff}.''')
