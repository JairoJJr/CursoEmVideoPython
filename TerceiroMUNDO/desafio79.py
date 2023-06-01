'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exita lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

num = []
while True:
    n = int(input("Digite um número: "))
    if n in num:
        print("Valor repetido")
    else:
        num.append(n)
    resp = str(input("Deseja inserir outro? [s/n]")).lower()
    while resp not in 'sn':
        resp = str(input("Dado inválido. Digite [s/n]")).lower()
    if resp == "n":
        break
num.sort()
print(num)
