'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

numeros = (int(input("Digite um número: ")),
           int(input("Digite outro número: ")),
           int(input("Digite mais um número: ")),
           int(input("Digite o último número: ")))

print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 not in numeros:
    print(f'O número 3 não foi digitado em nenhuma posição.')
else:
    print(f'O número 3 está na {numeros.index(3)+1}ª posição.')
ct = 0
for n in numeros:
    if n % 2 == 0:
        ct += 1
if ct != 0:
    print("Os números pares são: ",end=" ")
for n in numeros:    
    if n % 2 == 0:
        print(n, end = ' ')
    


