V1 =input("digite qualquer coisa:")
a =(V1.isalnum())
b = (V1.isalpha())
c = (type(V1))
d = (V1.isnumeric())

print(f'\033[7m{a}\033[m')
print(f'\033[1;34;41m{b}\033[m')
print(f'\033[4;31;44m{c}\033[m')
print(f'\033[7m{d}\033[m')


# \033[style(0'nada', 1'bold', 4'underline' e 7'inverte') , texto(números 30 a 37), back(números 40 a 47)]6