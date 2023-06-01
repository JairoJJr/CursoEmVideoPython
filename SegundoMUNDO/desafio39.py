'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

import datetime

nasc = int(input('Qual ano você nasceu? '))
idade = int(datetime.date.today().year) - nasc 
print(idade)

if idade <= 18:
    print(f'Faltam {18 - idade} anos para você se alistar')
elif idade == 18:
    print('Está na hora de você se alistar')
else:
    print(f'Você deveria ter se alistado há {idade - 18} ano(s) atrás.')


#usei a biblioteca datetime para encontrar a data atual, encontrei o ano em string e transformei em inteiro para descubrir a idade. 