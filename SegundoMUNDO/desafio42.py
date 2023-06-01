'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

seg1 = float(input("Digite o primeiro seguimento: "))
seg2 = float(input("Digite o segundo seguimento: "))
seg3 = float(input("Digite o terceiro seguimento: "))

if seg1 + seg2 < seg3:
    print("Não podem formar um triângulo.")
elif seg1 + seg3 < seg2:
    print("Não podem formar um triângulo.")
elif seg2 + seg3 < seg1:
    print("Não podem formar um triângulo.")
else:
    print("Podem formar um triângulo ", end = '')

    if seg1 == seg2 == seg3:
        print("EQUILÁTERO.")
    elif seg1 == seg2 != seg3 or seg2 == seg3 != seg1 or seg1 == seg3 != seg2:
        print("ISÓCELES.")
    else:
        print("ESCALENO.")

