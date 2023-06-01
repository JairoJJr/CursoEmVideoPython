'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado 
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
obs: Considere que o caixa possui cédulas de R$50,00, R$20,00, R$10,00 e R$1,00.'''

valor = int(input("Qual o valor a ser sacado: R$"))

cinquenta = valor // 50
vinte = (valor - (cinquenta*50)) // 20
dez = (valor - (vinte*20 + cinquenta*50)) // 10
um = (valor - (dez*10 + vinte*20 + cinquenta*50)) // 1

if cinquenta > 0:
    print(f'{cinquenta} notas de R$50,00')
if vinte > 0:
    print(f'{vinte} notas de R$20,00')
if dez > 0:
    print(f'{dez} notas de R$10,00')
if um > 0:
    print(f'{um} notas de R$1,00')
print(f'Para completar R${valor},00')

