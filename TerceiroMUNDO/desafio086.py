'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]

for c in range (0,3):
    for i in range (0,3):
        matriz[c][i].append(int(input(f'Digite o valor da posição {c + 1,i + 1}: ')))
for c in range (0,3):
    for i in range (0,3):
        print(matriz[c][i], end='')
    print()
    