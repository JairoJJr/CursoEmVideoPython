'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for c in range (0,3):
    for i in range (0,3):
        matriz[c][i]=(int(input(f'Digite o valor da posição {c + 1,i + 1}: ')))
for c in range (0,3):
    print('|',end='')
    for i in range (0,3):
        print(f'{matriz[c][i]:^5}', end='')
    print('|')
    