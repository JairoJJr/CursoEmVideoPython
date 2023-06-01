'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

n1 = int(input('Digite seu número: '))
d = n1 * 2
t = n1 * 3
rq = n1**(1/2)
print('O dobro do seu número {} é {}, o triplo é {} e a sua raiz quadrada é {:.3f}.'.format(n1, d,t,rq))

