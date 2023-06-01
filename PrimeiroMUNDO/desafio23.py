n = (input("Digite um número de 0 a 9999: "))
z = '000'+n

print('Unidade : {}'.format(z[-1]))
print('Dezena : {}'.format(z[-2]))
print('Centena : {}'.format(z[-3]))
print('Milhar : {}'.format(z[-4]))