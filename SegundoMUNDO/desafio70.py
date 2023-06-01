'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá preguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1.000,00.
C) Qual é o nome do produto mais barato.'''

s = ctmil = ct = 0

while True:
    nome = str(input("Produto: "))
    preco = float(input("Preço: "))
    ct += 1

    s += preco
    
    if preco > 1000:
        ctmil += 1
    if ct == 1 or preco < preco_menor:
        nome_mais_barato = nome
        preco_menor = preco
 
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Deseja inserir mais algum produto? [S/N]")).upper().strip()[0]

    if continuar == "N":
        break
    

print(f'Total da compra: {s:.2f}')
print(f'Quantidade de produtos que custam mais de R$1.000,00: {ctmil}')
print(f'Produto mais barato: {nome_mais_barato}')