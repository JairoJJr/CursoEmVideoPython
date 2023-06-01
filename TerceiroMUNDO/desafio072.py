'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso'''

ext = ('zero','um','dois','três','quatro','cinco','seis',
       'sete','oito','nove','dez','onze','doze','treze',
       'quatorze','quinze','dezesseis','dezesete',
       'desoito','dezenove','vinte')
while True:
    num = int(input("Digite um número de 0 a 20: "))
    while num > 20 or num < 0:
        num = int(input("Dado inválido, digite de 0 a 20: "))
    print(f'Você digitou o número {ext[num]}.')
    
    while True:
        resp = str(input("Deseja continuar? [S/N]")).strip().lower()
        if resp in "sn":
            break
    if resp == 'n':
        break
print('FIM')