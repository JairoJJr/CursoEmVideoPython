'''Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

aluno = {'nome' : '' , 'media' : '' , 'situacao' : '' }

aluno['nome'] = str(input('Qual o nome do aluno: ')).title()
aluno['media'] = float(input('Qual a média do aluno: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado!'
else:
    aluno['situacao'] = 'Reprovado!'

print(f'O aluno {aluno["nome"]} ficou com a nota {aluno["media"]:.1f} e está {aluno["situacao"]}')