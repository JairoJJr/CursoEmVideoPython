'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescentem além da idade, com quqantos anos a pessoa vai se aposentar.(35 anos de contribuição)'''

import datetime

cadastro = dict()

cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cadastro['Idade'] = datetime.datetime.now().year - nasc
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = f'R${float(input("Salário: R$")):.2f}'
    cadastro['Aposentadoria'] = (cadastro['Contratação'] + 35) - nasc

for k, v in cadastro.items():
    print(f'->{k:>15}:{v:>15}')