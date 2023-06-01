'''Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

import random 

print('''===========================
===O JOGO DA ADIVINHAÇÃO===
===========================''')

init = str(input('''Sou seu COMPUTADOR!
Você quer jogar um jogo de
adivinhação comigo? [S/N]''')).upper().strip()[0]

while init not in 'SN':
    init = str(input("Resposta inválida. Digite 'S' ou 'N':")).upper().strip()[0]

while init == 'S':  
    acertou = False
    ctt = 0
    num = random.randint(0,10)
    print(num)
    print('Eu pensei em um número de 0 a 10, tente adivinhar qual foi.')
    while not acertou:
        print(f'======={ctt+1}ª TENTATIVA=======')
        palp = int(input('Digite seu palpite:'))
        while not -1 < palp < 11:
            palp = int(input('''XxX-VALOR INVÁLIDO-XxX

Digite um valor entre 0 e 10: '''))
        ctt += 1 
        if palp == num:
            acertou = True
        else:
            print('''
xXxX-Resposta errada-xXxX''')
            if palp < num:
                print(f'''-----------DICA-----------
--O número que eu pensei--
------é MAIOR que {palp}.------
--------------------------''')
            else:
                print(f'''-----------DICA-----------
--O número que eu pensei--
------é MENOR que {palp}.------
--------------------------''')
    print('=====ACERTOU MISERÁVI=====')
    init = str(input(f'''-----O número era {num}----- 
Você acertou em {ctt} tentativas!
Quer jogar de novo? [S/N]: ''')).upper().strip()[0]
    

print('========GAME OVER========')
