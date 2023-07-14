'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
ex: 
n = leiaInt('DIGITE UM NÚMERO')'''

def LeiaInt(msg):
    """
    Lẽ apenas se for numérico
    :param n: dado inserido pelo teclado para validação.
    :return: Erro em caso de não numérico e o número caso for."""
    n = input(msg)
    while True:
        if n.isnumeric():
            return(f'Você digitou {n}')
            break
        else:
            print('\033[0;31mERRO, não é um número\033[m')
            n = input('Digite um número: ')


#Programa Principal
print(LeiaInt('Digite um número: '))