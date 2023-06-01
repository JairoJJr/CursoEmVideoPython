''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

preço = float(input("Digite o valor total da compra: "))
print('''Pagamento:\n
    [1] = à vista\n
    [2] = à vista no cartão\n
    [3] = em até 2x no cartão\n
    [4] = 3x ou mais no cartão\n''')
fp = int(input('Digite a forma de pagamento:'))

if fp == 4:
    p = int(input("Número de parcelas parcelas: "))

if fp == 1:
    print(f'Com 10% de desconto à vista, sua compra fica R${(preço - preço*0.1):.2f}.')
elif fp == 2:
    print(f'Com 5% de desconto à vista no cartão, sua compra fica R${preço - preço*0.05:.2f}.')
elif fp == 3:
    print(f'Sua compra fica em 2 vezes de R${preço/2:.2f} totalizando R${preço:.2f}.')
elif fp == 4:
    print(f'Sua compra fica em {p} vezes de R${(preço*1.2)/p:.2f} totalizando R${preço*1.2:.2f}.')
else:
    print('Opção inválida')

#Aqui eu usei formatação de string dentro do format nas chaves para determinar quantas casas após a vírgula o programa retornará.