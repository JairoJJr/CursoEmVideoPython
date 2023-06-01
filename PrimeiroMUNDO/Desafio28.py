import random as rnd
import os
rn = rnd.randint(0,5)
rnmais = rn + 2
rnmenos = rn - 2


def jogo():
    resp2 = int(input('OK! Eu estou pensando em um número de 0 a 5, adivinha qual é:'))
    if resp2 == rn:
        os.system("cls")
        print('UAL!! Era o número {} mesmo! Você é um vidente!!'.format(rn))
    elif resp2 >= 6:
        os.system("cls")
        print('EI! ENTRE 0 E 5!!')
        jogo()
    else:
        os.system("cls")
        resp3 = int(input('   AAhh que pena! Não era esse, vou te dar a última chance!\n'
                              '   Agora com uma dica: o meu número está entre os números {} e {},\n'
                              '   Mas não é maior que 5 e nem menor que 0. Qual é?'.format(rnmenos, rnmais)))
        if resp3 == rn:
            os.system("cls")
            print('Agora Sim!! Parabéns!! {} era meu número!'.format(rn))
        else:
            os.system("cls")
            print('Acabaram as chances!, o número era {}, \n'
                      'Ganhei de você ;D'.format(rn))

nome = str(input('Oi, Qual é seu nome?'))
os.system("cls")

resp = str(input('Olá {} Que nome Legal! Quer jogar um jogo de adivinhação comigo? [S/N]'.format(nome)))
if resp.lower() == 's':
    os.system("cls")
    jogo()
elif resp.lower() == 'n':
    os.system("cls")
    print('Tudo bem... Sem Graça... :(')

else:
    os.system('cls')
    str(input('DIGITE S OU N [S/N]'))


print('---FIM---')
os.system('PAUSE')


