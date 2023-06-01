'''Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que usando um laço for.'''

num = int(input("Digite um número inteiro. "))
mult = 0
for c in range(0,11):
    tab = mult * num
    print(f"{num} * {mult} = {tab}")
    mult += 1
    
