'''Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(txt):
    print('-'*20)
    print(txt)
    print('-'*20)


escreva(str(input("Digite uma frase: ")))