'''Interactive Helps'''

#help(print)
#print(print.__doc__)

'''DocStrings'''

#Uma linha depois da função acrescentar um coomentário com três áspas duplas, dessa forma o comando help() lê. EX:

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem;
    :param f: fim da contagem;
    :param p: passo da contagem;
    :return: sem retorno
    Função de Exemplo
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print("FIM!")

#help(contador) 

'''Parâmetros opcionais:
    função(a=0, b=0, c=0)'''

'''Escopos de variáveis:'''

def teste():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
teste()
print(f'N1 fora vale {n1}')

'''Comando return retorna o valor das variáveis. Bom para colocar dentro de uma função que vai ser armazenada em uma variável.'''

def fatorial(num=0):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input("Digite um número: "))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')
