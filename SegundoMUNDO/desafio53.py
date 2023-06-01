'''Crie um programa que leia uma frase qualquer e diga se  ela é um palíndromo, desconsiderando os espaços. 
Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA. Usando o FOR'''

frase = str(input("DIGITE UMA FRASE: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range (len(junto) - 1, -1, -1):   #len contou o número de caracteres, tira um pq range começa em 0, e o passo -1 é pq ta voltando
    inverso += junto[letra]                    #dentro do colchetes vai um número, para decidir qual caracter está selecionado daquela variável 

print(f'O inverso de {junto} é {inverso}, portanto')

if junto == inverso:
    print('a frase é um palíndromo.')
else:
    print('a frase não é um palínfromo.')


#inverso = junto[::-1]            poderia usar isso invés do for