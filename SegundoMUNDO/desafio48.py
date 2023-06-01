'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
 e que se encontram no intervalo de 1 até a 500'''

soma = 0
cont = 0

for c in range(3,501,2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma dos {cont} valores que foram solicitados é {soma}.')
print("FIM")