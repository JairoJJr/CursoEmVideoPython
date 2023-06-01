'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999.
No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

ct = 0
num = 0
soma = 0

while num != 999:
    num = int(input("Digite um número qualquer: [999 para parar] "))
    if num != 999:
        soma += num
        ct += 1
print(f'Você digitou um total de {ct} números e a soma entre eles é {soma}.')