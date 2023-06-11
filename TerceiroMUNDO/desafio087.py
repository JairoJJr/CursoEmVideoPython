'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]
somapares = 0
somaterceira = 0
mv = 0

for l in range (0,3):
    for c in range (0,3):
        n = int(input(f'Digite o valor da posição {l + 1,c + 1}: '))
        matriz[l][c].append(n)
        if n % 2 == 0:
            somapares += n
        if c== 2:
            somaterceira += n
        if c == 0 and l == 1:
            mv = n
        if c > 0 and l == 1:
            if n > mv:
                mv = n
        
print("A MATRIZ digitada foi:")
for c in range (0,3):
    for i in range (0,3):
        print(matriz[c][i], end='')
    print()
print(f'A soma dos valores pares é {somapares}.')
print(f'A soma dos valores da terceira coluna é {somaterceira}')
print(f'O maior valor da segunda linha é {mv}')
