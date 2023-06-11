'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta.
No final, mostre um boletim contando a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.'''

lista = []
aluno = []
resp = 's'
while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    aluno.append(float(input('Digite a primeira nota: ')))
    aluno.append(float(input('Digite a segunda nota: ')))
    lista.append(aluno[:])
    
    
    resp = str(input('Deseja inserir outro aluno?[S/N]:')).strip().lower()
    while resp not in 'sn':
        resp = str(input('Dado inválido, digite S ou N.'))
    if resp == 'n':
        break

print(aluno)