'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
 o aumento é de 15%.'''

s = float(input('Qual seu salário: '))
a10 = s * 1.1
a15 = s * 1.15

if s <= 1250:
    print(f'Seu aumento foi de 15% totalizando um salário de R${a15:.2f}')
else:
    print(f'Seu aumento foi de 10% totalizando um salário de R${a10:.2f}')