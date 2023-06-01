'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''


n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual a sua segunda nota? '))
n3 = float(input('Qual a sua terceira nota? '))

m = (n1 + n2 + n3)/3

if m <= 4.9:
    print(f'Sua média foi {m:.1f} e você foi \033[31mREPROVADO\033[m.')
elif 7 > m >= 5:
    print(f'Sua média foi {m:.1f} e você está de \033[34mRECUPERAÇÃO\033[m.')
else:
    print(f'Parabéns! Sua média foi {m:.1f} e você foi \033[32mAPROVADO\033[n!')



#USEI COMANDOS PARA TREINAR CORES NO TERMINAL
