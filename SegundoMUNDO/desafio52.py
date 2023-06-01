'''Faça um programa que leia um número inteiro e  diga se ele é ou não um número inteiro.'''

n = int(input("Digite um número inteiro: "))
d = []

for c in range (1 , n +1):
    if n % c == 0:
        d.append(c)                                           #usei o cod APPEND para inserir elementos na lista.
if len(d) > 2:
    print(f"{n} é divisível por", *d, sep = ' ')              #usei o * ou unpack para tirar os colchetes na saída da lista. Torna str
    print(f'Por isso {n} não é um número primo')
else:
    print(f'{n} é um número primo.')
