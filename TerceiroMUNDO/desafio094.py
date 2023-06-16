'''Crie um programa que leia nome, sexo e idade de várias pessoas guardando os dados de cada pessoa em um dicionário e todos
os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.'''

cadastros = list()
pessoa = dict()
resp = 's'
soma = media = 0
idade_acima = list()
while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).strip().upper()
        if pessoa['Sexo'] in 'MF':
            break
        print('Dado inválido. Digite M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    cadastros.append(pessoa.copy())
    pessoa.clear()

    while True:
        resp = str(input("Deseja continuar? [S/N]")).strip().lower()
        if resp in 'sn':
            break
        print(("Dado inválido. Digite S ou N. "))
    if resp == 'n':
        break
        
print('=-*20')
print(f'A) Foram cadastradas {len(cadastros)} pessoas.')
media = soma / len(cadastros)
print(f'B) A média das idades é {media:.2f} anos.')
print(f'As mulheres cadastradas são ' , end = '')
for p in cadastros:
    if p['Sexo'] == "F":
        print(f'{p["Nome"]}' , end = ' ')
    print()
print(f'Lista das pessoas que estão acima da média: ')
for p in cadastros:
    if p['Idade'] > media:
        for k , v in p.items():
            print(f'{k} = {v}; ', end = ' ')
        print()
        
