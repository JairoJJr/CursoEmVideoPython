'''Aprimore o desafio 93 para que ele funcione com váarios jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

'''93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = dict()
time = list()
partidas = list()

while True:
    jogador["Nome"] = str(input("Nome: "))
    jogador["Número de Partidas"] = int(input("Número de partidas: "))
    for c in range(0 , jogador["Número de Partidas"]):
        partidas.append(int(input(f"Quantos gols na {c+1}ª partida?")))    
    jogador['Gols Partida'] = partidas[:]
    jogador['Total'] = sum(partidas)
    partidas.clear()
    time.append(jogador.copy())
    jogador.clear()
    while True:
        resp = str(input("Quer continuar? [S/N]")).upper()[0]
        if resp in 'SN':
            break
        print('Dado inválido, digite S ou N.')
    if resp == 'N':
        break
print('=-'*20)
print('cod  ' , 'Nome' , ' '*15 , 'Gols' , ' '*15 , 'Total')
print('-'*20)
for k, v in enumerate(time):
    print(f'{k:>4}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}' , end = ' ')
    print()
print('=-'*20)
    
    
        