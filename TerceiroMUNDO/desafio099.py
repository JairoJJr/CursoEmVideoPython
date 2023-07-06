'''Faça um programa que tenha uma função maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(lst):
    for i in lst:
        if i == 1:
            nM = i
        else:
            if i > nM:
                nM = i
    print(nM)
    

lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    resp = str(input("Deseja colocar outro número? [S/N]")).lower().strip()
    if resp == 'n':
        break
maior(lista)

