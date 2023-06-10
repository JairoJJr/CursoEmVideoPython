'''Crie um programa que vai ler vários números e colocar numa lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma descrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

num = []
ct = 0
while True:
    ct += 1

    num.append(int(input("Digite um número: ")))
    resp = str(input("Deseja inserir mais um número? [S/N]")).strip().upper()
    while resp not in 'SN':
        resp = str(input("Dado inválido, digite S ou N: ")).strip().upper()
    if resp == "N":
        break
print(f'Foram digitados {len(num)} números.')
ordem = sorted(num, reverse=True)
print(f'Que são {ordem}')
if 5 in num:
    print(f'Existem {num.count(5)} números 5 na lista.')