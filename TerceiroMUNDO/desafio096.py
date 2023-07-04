'''Faça um programa que tenha uma funçãochamada área(), que receba as dimensões de um terreno
(largura e comprimento) e mostre a área do terreno.'''

def area(C , L):
    a = C * L
    print(f'A área de um terreno de {C}m por {L}m é de {a}m.')

area(
    int(input('Qual o comprimento do terreno? (Metros) ')),
    int(input('Qual a largura do terreno? (Metros)'))
)