'''Faça um programa que leia uma frase pelo teclado e mostre quantas
vezes aparece a letra "A", em que posição ela aparece a primeira vez
 e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).strip().lower() #strip tira espaços antes e depois
print(f'A letra A aparece {frase.count("a")} vezes na frase.')
print(f'A primeira letra A está na posição {frase.find("a") + 1}.')
print(f'A última letra A aparece na posição {frase.rfind("a") + 1}')

print(frase)

