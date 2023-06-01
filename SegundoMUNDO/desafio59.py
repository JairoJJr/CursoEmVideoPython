'''Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

n1 = int(input("Digite seu primeiro valor: "))
n2 = int(input("Digite seu segundo valor: "))
opcao = 0
while opcao != 5:
    sleep(1)
    print(16*'=-=')
    opcao = int(input('''O que você quer fazer?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    '''))
    print(16*'=-=')
    
    if opcao == 1:
        print('Calculando', end = '')
        sleep(0.5)
        print('.', end = '')
        sleep(0.5)
        print('.', end = '')
        sleep(0.5)
        print('.')
        sleep(0.5)
        s = n1 + n2
        print(f'O valor da soma entre {n1} e {n2} é igual a {s}.')
    elif opcao == 2:
        print('Calculando', end = '')
        sleep(0.5)
        print('.', end = '')
        sleep(0.5)
        print('.', end = '')
        sleep(0.5)
        print('.')
        sleep(0.5)
        m = n1 * n2
        print(f'O valor da multiplicação entre {n1} e {n2} é {m}.')
    elif opcao == 3:
        print('Calculando', end = '')
        sleep(0.5)
        print('.', end = '')
        sleep(0.5)
        print('.', end = '')
        sleep(0.5)
        print('.')
        sleep(0.5)
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.')
        else:
            print(f'Os valores {n1} e {n2} são iguais.')
    elif opcao == 4:
        n1 = int(input("Digite seu primeiro valor: "))
        n2 = int(input('Digite seu segundo valor: '))
    elif opcao == 5:
        print('Finalizando', end = '')
        sleep(0.5)
        print('.', end = '')
        sleep(0.5)
        print('.', end = '')
        sleep(0.5)
        print('.')
        sleep(0.5)
    else:
        print("OPÇÃO INVÁLIDA, tente novamente.")

print('FIM')