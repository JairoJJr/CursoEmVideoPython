'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão. Usando FOR.'''

pt = int(input("Digite o primeiro termo da PA, sendo um número inteiro."))
rpa = int(input("Agora digite a razão da PA desejada."))
dec = pt + (10-1) * rpa  #fórmula do último termo ulttermo = primtermo + (ntermos - 1) * razão

for c in range (pt , dec + rpa, rpa):
    print(f'{c}', end = ' -> ')
print ("ACABOU")