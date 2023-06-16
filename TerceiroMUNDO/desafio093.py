'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = dict()

jogador['Nome'] = str(input("Nome: ")).title()
jogador['Número de Partidas'] = int(input("Número de partidas: "))

jogador['Total de Gols'] = 0
for c in range(0, jogador['Número de Partidas']):
    jogador[f'Partida {c+1}'] = int(input(f'Quantos Gols fez na {c+1} partida:'))
    jogador['Total de Gols'] += jogador[f'Partida {c+1}']

print('=-'*20)
for k, v in jogador.items():
    print(f'=>{k:>20}:{v:>10}.')