from time import sleep
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print("\033[31mERRO\033[m")
            continue
        else:
            return num


def linha(tam = 42):
    return "-"*tam


def cab(txt):
    sleep(1)
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cab('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc