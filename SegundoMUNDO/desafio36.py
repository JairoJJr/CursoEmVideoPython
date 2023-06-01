'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado'''

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
tempo = float(input('Em quantos anos você quer pagar? '))

parcela = casa / (tempo*12)

if parcela >= salario * 0.3:
    print(f'Para comprar uma casa de R${casa:.2f} a parcela ficaria em R${parcela:.2f}, seu salário não é compatível com o valor da parcela.\n Empréstimo NEGADO')
else:
    print(f'Sua parcela ficará no valor de R${parcela:.2f}\nEmpréstimo CONCEDIDO.')