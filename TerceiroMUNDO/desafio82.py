'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

num = []
numpar = []
numimp = []
ct = 0
while True:
    num.append(int(input("Digite um número: ")))
    resp = str(input("DEseja inserir outro? [S/N]")).strip().lower()
    if num[ct] % 2 == 0:
        numpar.append(num[ct])
    else:
        numimp.append(num[ct])
    while resp not in "sn":
        resp = str(input("Dado inválido, digite S ou N")).strip().lower()
    if resp == "n":
        break
    ct += 1
print(num , numpar , numimp)
