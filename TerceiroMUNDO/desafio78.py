'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçóes na lista.'''
num = []
mainum = mennum = 0
for i in range(0, 5):
    num.append(int(input("Digite um número: ")))
    if i == 0:
        mainum = mennum = num[0]
        pmen = pmai = i + 1
    else:
        if num[i] < mennum:
            pmen = i +1
            mennum = num[i]
        if num[i] > mainum:
            pmai = i + 1
            mainum = num[i]
print(f'O maior número foi {mainum} na posição {pmai} e o menor foi {mennum} na posição {pmen}.')



#Esqueci de mostrar as posições, voltar para arrumar
