'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um DICIONÁRIO
com as seguintes informações:
- Quantidade de  notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicionne também as DocString na função'''

def notas(*num , sit=False):
    """
    Recebe várias notas e é capaz de calcular o maior, o menor e a média dos valores.
    :param num: Lista de notas.
    :param sit: Mostrar ou não a situação.
    :return: Um dicionário com todas as informações a cima.
    """
    r = dict()
    r['Total'] = len(num)
    r['Maior'] = max(num)
    r['Menor'] = min(num)
    r['Média'] = sum(num)/len(num)
    if sit == True:
        if float(r['Média']) < 6:
            r['Situação'] = 'Ruim'
        if float(r['Média']) > 7:
            r['Situação'] = 'Boa'
        else:
            r['Situação'] = 'Razoável'
    return(r)


#Prograrma Principal
resp = notas(10, 9, 1.5, 6, 9, sit=True)
print(resp)

