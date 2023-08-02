from libb.interface import cab


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('\033[31mHouve um Erro!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO!\033[m')
    else:
        cab('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mERRO!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mErro ao escrever no arquivo\033[m')
        else:
            print(f'Novo registro de {nome} adicionado')
    finally:
        a.close()