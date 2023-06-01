'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 

1 para binário, 2 para octal e 3 para hexadecimal.'''
num = int(input('Escreva um número '))

bin = bin(num)
oct = oct(num)
hex = hex(num)

print('''Escolha uma opção para conversão:
[1] para binário
[2] para octal
[3] para hexadecimal''')

opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'A conversão binária do número {num} é {bin[2:]}.')          #usei fatiamento de string para ignorar os dois primeiros dígitos da informação.
elif opcao == 2:
    print(f'A conversão octal do número {num} é {oct[2:]}.')
elif opcao == 3:
    print(f'A conversão hexadecimal do número {num} é {hex[2:]}.')
else:
    print('Opção inválida.')