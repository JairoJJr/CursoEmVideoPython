'''Aula sobre rotinas (Funções)'''
def linha(msg):
    print('=-'*20)
    print(msg)
    print('=-'*20)

linha("     Primeiro Exemplo")
def titulo(txt):
    print('-'*20)
    print(txt)
    print('-'*20)

titulo('    Aula 20')
titulo('    Deu certo')

linha("     Exemplo com função soma")
def soma(a, b):
    print('-'*20)
    print(f'A vale {a} e B vale {b}.')
    print(f'A soma A + B é {a + b}.')
    print('-'*20)

#Programa Principal soma
soma(4, 5)
soma(8, 9)
soma(2, 1)

linha('     Exemplo com função contador')
def contador(*num):
    print('Recebi os valores: ', end='')
    for v in num:
        print(f'{v}', end=' ')
    print(f'e são ao todo {len(num)} números.')


#Programa Principal contador
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

linha('     Exemplo com Lista dentro da Função (dobrando valores)')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)