'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o NÚMERO a calcular e o outro chamado SHOW, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n=0 , show=False):
    """
    Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não o cálculo.
    :return: O valor do fatorial de um número n."""
    
    f = 1
    for i in range (n, 0, -1):
        f *= i
    if show == False:
        return(f'O fatorial de {n} é {f}')
    else:
        for i in range(n, 0, -1):
            if i != 1:
                print(i, end=' X ')
            else:
                print(i,' = ',f)


n = int(input('Digite um número: '))
while True:
    show = str(input('Ver cálculo? [S/N]: ')).lower().strip()
    if show not in 'sn':
        print('ERRO! Digite S ou N')
    else:
        if show == 's':
            show = True
            fatorial(n, show)
        else:
            show = False
            print(f'{fatorial(n , show)}')
        break


