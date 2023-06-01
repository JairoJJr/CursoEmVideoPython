'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome'''

nome = str(input("Qual é seu nome completo? ")).lower()

print(f'{"silva" in nome}')