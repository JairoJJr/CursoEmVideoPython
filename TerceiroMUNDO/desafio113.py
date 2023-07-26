'''Reescreva a função leiaInt() que fizemos no exercício 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade'''

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print("\033[31mERRO\033[m")
            continue
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except:
            print("\033[31mERRO\033[m")
            continue
        else:
            return num


Inteiro = leiaInt("Digite um número inteiro: ")
Real = leiaFloat("Digite um número Real: ")
print(f'O número inteiro digitado foi {Inteiro} e o real foi {Real}.')