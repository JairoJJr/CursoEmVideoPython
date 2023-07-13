'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGRATÓRIO  nas eleições.'''
import datetime

def voto(nasc):
    h = int(datetime.date.today().year)
    i = h - nasc
    if 18 <= i < 65:
        return(f"Com {i} anos o voto é OBRIGATÓRIO")
    elif i < 18:
        return(f"Com {i} anos o voto é NEGADO")
    else:
        return(f"Com {i} anos o voto é OPCIONAL")
    

#Programa Principal
nasc = int(input('Digite o ano de nascimento: '))
print(f'{voto(nasc)}')

