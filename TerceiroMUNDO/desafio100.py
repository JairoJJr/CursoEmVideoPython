'''Faça um programa que tenha uma lista chamada números e duas Funções chamada sorteio() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma  entre todos os valores Pares sorteados pela função anterior.'''

import random
import time

def sorteio(lst):
    print("Números escolhidos: ", end=' ')
    for i in range (0, 5):
        lst.append(random.randint(0,100))
        print(lst[i], end = ' ')
        time.sleep(1/2)

def somaPar(lst):
    soma = 0
    print("A soma dos pares que foram sorteados é: ", end = ' ')
    for i in lst:
        if i % 2 == 0:
            soma += i
    print(soma)

lista = []

sorteio(lista)
print('')
somaPar(lista)
