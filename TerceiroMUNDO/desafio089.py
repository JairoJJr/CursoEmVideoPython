'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.'''

lista = []
aluno = []
resp = 's'
while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    aluno.append(float(input('Digite a primeira nota: ')))
    aluno.append(float(input('Digite a segunda nota: ')))
    aluno.append((aluno[1]+aluno[2])/2)
    lista.append(aluno[:])
    aluno.clear()
    
    resp = str(input('Deseja inserir outro aluno?[S/N]:')).strip().lower()
    while resp not in 'sn':
        resp = str(input('Dado inválido, digite S ou N.'))
    if resp == 'n':
        break
print('=-'*6,'BOLETIM','=-'*6)
print()
print('=-=NOME=-=NOTA1=-=NOTA2=-=MÉDIA=-=')
print()
for i, item in enumerate(lista):
    print(i+1,end=' ')
    for c in range(0,4):
        print(f'{lista[i][c]:^7}',end=' ')
    print()
print()
resp = 's'
while True:
    consulta = int(input('Digite o número do aluno que deseja consultar: '))
    print()
    print('=-=NOME=-=NOTA1=-=NOTA2=-=MÉDIA=-=')
    print(consulta,end=' ')
    for c in range(0,4):
        print(f'{lista[consulta-1][c]:^7}',end=' ')
    print()
    print()
    resp = str(input('Deseja consultar outro aluno?[S/N]:')).strip().lower()
    while resp not in 'sn':
        resp = str(input('Dado inválido, digite S ou N.'))
    if resp == 'n':
        break
print('=-=FIM=-=')
    