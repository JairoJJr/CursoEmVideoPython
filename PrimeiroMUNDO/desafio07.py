'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print('A sua média é', m)
if m > 6:
    print('Parabéns! Você está acima da média!!')
elif m == 6:
    print('Cuidado! A sua nota é média!')
else:
    print('Sua nota foi ruim! Estude mais!')

