'''Crie um programa onde o úsuário possa digitar 7 valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

num = [[],[]]

for c in range (0,7):
    n  = int(input(f"Digite o {c+1}º número: "))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

num[0].sort()
num[1].sort()

print(f'Os números pares são {num[0]}')
print(f'Os valores ímpares são {num[1]}')
    
