'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

num1 = int(input("Digite um número inteiro: "))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print(f'O primeiro número {num1} é maior que o segundo número {num2}.')
elif num2 > num1:
    print(f'O segundo número {num2} é maior que o primero número {num1}.')
else:
    print(f'O primeiro número {num1} e o segundo {num2} são iguais.') 