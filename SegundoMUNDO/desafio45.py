'''Crie um programa que faça o computador jogar Jokenpô com você.'''

import time

print("Esse é um jogo de JO-KEN-POH! ")


iniciar = str(input("Vamos Jogar? [S / N]")).upper()
reset = iniciar
itens = ('nada' , 'Pedra', 'Papel' , 'Tesoura')
while reset == "S":

    import random
        #Jogada do PC
    jpc = random.randint(1,3)

        #Jogada do Jogador
    jjg = int(input('''Qual sua jogada?:
        [1] Pedra
        [2] Papel
        [3] Tesoura
        '''))
    
    print("JO!")
    time.sleep(1)
    print("KEN!")
    time.sleep(1)
    print("POH!")
    time.sleep(1)

    print(f'Sua Jogada foi {itens[jjg]} e a do Computador foi {itens[jpc]}')


            
    if jpc == 1 and jjg == 1:
        print("Empate!")
    elif jpc == 1 and jjg == 2:
        print("Você venceu o Computador!")
    elif jpc == 1 and jjg == 3:
        print("Você Perdeu do Computador!")
    elif jpc == 2 and jjg == 1:
        print("Você perdeu do Computador!")
    elif jpc == 2 and jjg == 2:
        print("Empate!")
    elif jpc == 2 and jjg == 3:
        print("Você venceu o Computador!")
    elif jpc == 3 and jjg == 1:
        print("Você venceu o Computador!")
    elif jpc == 3 and jjg == 2:
        print("Você perdeu do Computador!")
    else:
        print("Empate!")
    reset = input('Continuar a jogar?[S/N]').upper()


print("GAME OVER!")