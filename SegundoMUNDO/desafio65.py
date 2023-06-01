'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

num = 0
ct = 0
mv = 0
MV = 0
con = 's'
soma = 0

while con != "n":
    num = (int(input("Digite um número inteiro: "))) 
    soma += num
    ct += 1
    if ct == 1:
        mv = num
        MV = num
    else:
        if num < mv:
            mv = num
        elif num > mv:
            MV = num
    con = (str(input("Deseja continuar? [S/N]: "))).lower()
media = soma / ct
print(f'A média dos valores que você digitou é {media} sendo o maior valor {MV} e o menor valor {mv}.')
