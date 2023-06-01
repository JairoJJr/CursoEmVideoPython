'''Faça um programa que jogue par ou ímpar  com o computador.
O programa só será interrompido quando o jogador perder, mostrando total de vitórias consecutivas
que ele conquistou no final do jogo.'''

import random 

ct = 0

print('==-=-=-==Vamos jogar Par ou Ímpar!==-=-=-==')
while True:
    npc = random.randint(1,2)
    #print(npc)
   
    opcj = str(input("Escolha par ou ímpar. [P/I]")).upper().strip()[0]
    while opcj not in "PI":
        opcj = str(input("Resposta inválida, tente novamente: ")).upper().strip()[0]
    
    nj = int(input('Digite um número de 0 até 9: '))
    while nj < 0 or nj > 9:
        nj = int(input('Reposta inválida, tente novamente um número de 0 até 9: '))

    if opcj == 'P':
        if (npc + nj) % 2 == 0:
            print(f' O computador jogou {npc} e você {nj}. Você ganhou!')
            ct += 1

        else:
            print(f'O computador jogou {npc} e você {nj}. Você perdeu!')
            break
            
    if opcj == 'I':
        if (npc + nj) % 2 == 0:
            print(f'O computador jogou {npc} e você {nj}. Você perdeu!')
            break
        else:
            print(f'O computador jogou {npc} e você {nj}. Você ganhou!')
            ct += 1
    print(10*"-=-")       
    print('Bora de novo!')

print(f'GAME OVER! Você ganhou {ct} vezes consecutivas.')