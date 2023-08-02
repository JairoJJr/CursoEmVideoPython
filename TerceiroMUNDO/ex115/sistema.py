from libb.interface import *
from libb.arquivo import *
from time import sleep

#programa principal

arq = "bdados.txt"

if arqExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    criarArq(arq)

while True:
    resp = menu(['Consultar','Cadastrar','Sair'])
    if resp == 1:
        #Listar conteúdo
        lerArq(arq)
    elif resp == 2:
        cab('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resp == 3:
        cab('Saindo do sistema...')
        break
    else:
        print('\033[31mErro!\033[m')
        sleep(2)