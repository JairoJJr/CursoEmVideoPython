'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o menor valor que estão na tupla.'''

import random
numeros = random.randint(0,100) , random.randint(0,100) , random.randint(0,100) , random.randint(0,100) , random.randint(0,100) 
print(f'Os valores sorteados foram {numeros}')

#ordem = sorted(numeros)
#print(f'O maior valor sorteado foi: {ordem[-1]}')
#print(f'O menor valor sorteado foi: {ordem[0]}')

print(f'O maior valor foi {max(numeros)}')
print(f'O menor valor foi {min(numeros)}')