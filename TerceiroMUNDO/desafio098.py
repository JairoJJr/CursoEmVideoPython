'''Faça um programa que tenha uma função chamada contador()
que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10m de 1 em 1
B) de 10 até 0, de 2 em 2
C) Uma contagem personalizada.'''

def linha():
    print('-='*20)

def A():
    print('Contagem de 1 até 10 de 1 em 1:')
    for i in range(1, 11):
        print(i, end=' ')
    print('')

def B():
    print('Contagem de 10 até 0 de 2 em 2:')
    for i in range(10,-1,-1):
        print(i, end=' ')
    print('')

def C(inicio , fim , passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        for i in range(inicio , fim+1 , passo):
            print(i , end=' ')
        print('')
    elif inicio >= fim:
        for i in range(inicio , fim-1 , -passo):
            print(i , end = ' ')
        print('')        
        

linha()
A()
linha()
B()
linha()
print("Agora é sua vez de personalizar a contagem!")
C(int(input("Início: ")),
  int(input('Fim: ')),
  int(input('Passo: ')))
linha()