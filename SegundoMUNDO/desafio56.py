'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
-> A média de idade do grupo,
-> Qual é o nome do mais velho
-> E quantas mulheres têm menos de 20 anos'''

ihv = 0
hmv = "[Não há homens]"
ctm20 = 0
totidad = 0

for pess in range(1, 5):
    print(f'=========={pess}ª PESSOA==========')
    nome = str(input(f'Qual o nome da {pess}ª pessoa: '))
    idade = int(input(f'Qual a idade da {pess}ª pessoa: '))
    sexo = str(input(f'Qual o sexo da {pess}ª pessoa: [F/M]')).upper()
    
    totidad += idade
    m = totidad / pess

    if sexo == 'M':
        if idade > ihv:
            ihv = idade
            hmv = nome
    else:
        if idade < 20:
            ctm20 += 1
print(f'==========RESULTADO==========')
print(f'''A média de idade do grupo é {m},
O homem mais velho tem {ihv} anos e se chama {hmv.title()}
E têm {ctm20} mulheres menores de 20 anos.''')        




