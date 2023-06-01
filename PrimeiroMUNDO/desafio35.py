'''Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.'''

seg1 = int(input("Digite o primeiro seguimento: "))
seg2 = int(input("Digite o segundo seguimento: "))
seg3 = int(input("Digite o terceiro seguimento: "))

if seg1 + seg2 < seg3:
    print("Não podem formar um triângulo.")
elif seg1 + seg3 < seg2:
    print("Não podem formar um triângulo.")
elif seg2 + seg3 < seg1:
    print("Não podem formar um triângulo.")
else:
    print("Podem formar um triângulo.")
