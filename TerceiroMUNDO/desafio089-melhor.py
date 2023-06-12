'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.'''

lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    lista.append([nome,[nota1,nota2],media])
    resp = str(input('Deseja inserir outro aluno?[S/N]:')).strip().lower()
    while resp not in 'sn':
        resp = str(input('Dado inválido, digite S ou N.'))
    if resp == 'n':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":>10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(lista):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.2f}')
resp = 's'
while True:
    print('-' * 35)
    consultar = int(input('Digite o número do aluno que deseja consultar: ')) - 1
    print(f'Notas de {lista[consultar][0]} são {lista[consultar][1]}.')
    resp = str(input('Deseja inserir outro aluno?[S/N]:')).strip().lower()
    while resp not in 'sn':
        resp = str(input('Dado inválido, digite S ou N.'))
    if resp == 'n':
        break
print('=-=FIM=-=')

