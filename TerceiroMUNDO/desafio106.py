'''Faça um mini-sistema que utiliza o Interactive Help do Python. O usuário
vai digitar o comando e o manual vai aparecer.
Quanto o usuário digitar FIM, o programa se encerrará. '''


def ajuda(com):
    help(com)


#Programa principal
comando = ''

while True:
    comando = str(input("Função ou Biblioteca > ")).upper
    if comando == 'FIM':
        break
    else:
        ajuda(comando)
    
