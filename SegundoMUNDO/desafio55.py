'''Faça um programa que leia o peso de cinco pessoas. No final mostra qual foi 
o maior e o menos peso lidos.'''

pmaior = 0
pmenor = 0

for pessoas in range(1 , 6):
    peso = float(input(f'Digite o peso da {pessoas}ª pessoa:'))
    if pessoas == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        elif peso < pmenor:
            pmenor = peso
print(f'O maior peso digitado foi {pmaior:.2f}kg e o menor foi {pmenor:.2f}kg.')
