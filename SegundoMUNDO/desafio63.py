'''Escreva um programa que leia um número N inteiro
e mostre na tela os N primeiros elementos de uma SEQUÊNCIA DE FIBONACCI.
EX: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

ct = 0
terman = 0
terman1 = 1

termos = int(input("Digite quantos termos quer ver: "))

print(terman , end = '->')
print(terman1 , end = '->')
while ct != (termos - 2):
    F = terman + terman1
    terman = terman1
    terman1 = F
    print( F , end = '->')
    ct += 1
print("FIM")
    

    #FUNCIONOU MAS ELE FEZ DE OUTRO JEITO (DAR UMA OLHADA DEPOIS.)
