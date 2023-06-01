'''O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

#shuffle é embaralhar, usei o .title() fora do parenteses do input, usei o 'as' na importação.

from random import shuffle as sh
A1 = str(input('Primeiro aluno: ').title())
A2 = str(input('Segundo aluno: ').title())
A3 = str(input('Terceiro aluno: ').title())
A4 = str(input('Quarto aluno: ').title())

lista = [A1, A2, A3, A4]
sh(lista)
print(f'A ordem de apresentação será: {lista}')
