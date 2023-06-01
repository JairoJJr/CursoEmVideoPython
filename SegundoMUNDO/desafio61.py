'''refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da PA usando WHILE.
DESAFIO 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''

pt = int(input('Digite o primeiro termo: '))
rpa = int(input('Digite a razão da PA: '))
dec = pt + (10 - 1) * rpa

while pt != dec + rpa:
    print(pt , end = "->")
    pt += rpa
    
print("FIM") 