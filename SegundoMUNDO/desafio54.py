'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maior idade
e quantas já são maiores. '''

from datetime import date as dt

ctmaior = 0
ctmenor = 0

for pessoa in range(1, 8):
    nasc = int(input(f"Digite o ano de nascimento da {pessoa}ª pessoa: "))
    idade = dt.today().year - nasc
    pessoa += 1

    if idade >= 18:
        ctmaior += 1
    else:
        ctmenor += 1

print(f'{ctmenor} pessoas ainda não atingiram a maioridade e {ctmaior} pessoas já são maiores.')
    