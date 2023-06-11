'''Faça um programa que ajude um jogador da MEGASENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e 
vai sortear 6 números entre 1 e 60  para cada jogo, cadastrando tudo em uma lista composta.'''

import random as rd
import time

jogos = []
temp = []
r = int(input("Quantos jogos você quer? "))
for i in range(0 , r):    
    for c in range (0 , 6):
        n = rd.randint(0 , 60)
        while n in temp:
            n = rd.randint(0 , 60)
        temp.append(n)
        temp.sort()
    jogos.append(temp[:])
    temp.clear()
for j in range(0 , r):
    print('GERANDO.',end='')
    time.sleep(1/3)
    print('.',end='')
    time.sleep(1/3)
    print('.')
    time.sleep(1/3)
    print(f'{j+1}º Jogo: {jogos[j]}')
    time.sleep(1/3)
    