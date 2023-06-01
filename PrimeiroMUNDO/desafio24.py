'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO" '''

city = input('Digite o nome da cidade que você mora: ').lower()
s = city.find('santo ')
if s>= 0:
    print('A sua cidade leva o nome de um Santo')
else:
    print('A sua cidade não leva o nome de uma Santo')