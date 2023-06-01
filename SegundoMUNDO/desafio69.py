'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''

ct18 = 0
ctH = 0
ctM20 = 0

while True:
    idade = int(input('Digite a idade: '))
    while idade < 0:
         idade = int(input('Opção inválida. Tente novamente com uma idade possível: '))
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    while sexo not in 'MF':
         sexo = str(input('Opção inválida. Tente novamente. [M/F]')).upper().strip()[0]
    if sexo == 'M':
        ctH += 1
        if idade >= 18:
            ct18 += 1   
    if sexo == 'F':
        if idade < 20:
            ctM20 += 1
        if idade >= 18:
            ct18 += 1
    opcao = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    while opcao not in 'SN':
         opcao = str(input('Opção inválida. Tente novamente. [S/N]')).upper().strip()[0]
    if opcao == 'N':
                break
print(f'Vocẽ inseriu {ct18} pessoas com mais de 18 anos, {ctH} homens e {ctM20} Mulheres com menos de 20 anos.')



'''Para validar posso colocar o input apenas dentro do while, em cima declarar a variável vazia com ' ' '''