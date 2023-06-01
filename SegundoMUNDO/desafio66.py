'''Crie uma programa que leia vários números inteiros pelo teclado.
O program só vai parar quando o usuário digitar o valor 999,
que é a condiçpão de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando o flag)'''

ct = s = 0

while True:
    n = int(input("Digite um número inteiro: "))
    if n == 999:
        break
    ct += 1
    s += n

print(f'Foram digitados {ct} números e a soma entre eles é {s}.')
