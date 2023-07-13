'''Faça um programa que tenha uma função chamada ficha(), que tenha dois parâmetros opicionais:
o NOME de um jogador e quantos GOLS ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='<desconhecido>', gols = 0):
    return(f'O jogador {nome} fez {gols} gols.')


n = str(input('Nome do Jogador: ')).title()
g = str(input("Número de gols: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    print(ficha(gols = g))
else:
    print(ficha(n, g))