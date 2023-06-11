'''Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
Ao final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma lista com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = []
dado = []
mp = []
ml = []

while True:
    dado.append(str(input("Digite o nome: ")).title())
    dado.append(float(input("Digite o peso em kg: ")))

    if len(pessoas) == 0:
        mp.append(dado[:])
        ml.append(dado[:])
    else:
        if dado[1] > mp[0][1]:
            mp.clear()
            mp.append(dado[:])
        elif dado[1] == mp[0][1]:
            mp.append(dado[:])
        elif dado[1] < ml[0][1]:
            ml.clear()
            ml.append(dado[:])
        elif dado[1] == ml[0][1]:
            ml.append(dado[:])

    pessoas.append(dado[:])
    dado.clear()
            
    resp = str(input("Inserir outra pessoa? [S/N]")).strip().lower()
    while resp not in 'sn':
        resp = str(input("Dado inválido, digite S ou N.")).strip().lower()
    if resp == "n":
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')

if len(mp) > 1:
    for c in range (0, len(mp)):
        print(f'{mp[c][0]}', end= ", ")
    print(f'São as pessoas mais pesadas com {mp[0][1]}kg.')
else:
    print(f'{mp[0][0]} é a pessoa mais pesada com {mp[0][1]}kg.')

if len(ml) > 1:
    for c in range (0, len(ml)):
        print(f'{ml[c][0]}', end= ", ")
    print(f'São as pessoas mais leves com {ml[0][1]}kg.')
else:
    print(f'{ml[0][0]} é a pessoa mais leve com {ml[0][1]}kg.')