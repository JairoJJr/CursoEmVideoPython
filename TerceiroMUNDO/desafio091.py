'''Crie um programa onde quatro jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

import random as rd
import time
from operator import itemgetter  #ordenar dicionário

results= {}
jogador= []
for c in range(0,4):
    results[f'Jogador{c+1}'] = rd.randint(1,6)

ranking = {}

print('VALORES SORTEADOS:')
for k,v in results.items():
    print(f'{k} tirou {v}')
    time.sleep(1/3)

ranking = sorted(results.items() , key = itemgetter(1) , reverse=True)
print('=-' * 18)
print(f'    == RANKING DOS JOGADORES  ==')
for i, v in enumerate(ranking):
    print(f'     {i+1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(1/3)


