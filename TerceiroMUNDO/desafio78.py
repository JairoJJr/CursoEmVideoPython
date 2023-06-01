'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçóes na lista.'''
num = []
for i in range(0, 5):
    num.append(int(input("Digite um número: ")))
num.sort()
print(f'O maior número foi {num[-1]} e o menor foi {num[0]}')
