'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = str(input("Digite seu nome completo: ")).strip()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome completo em minúsculas é {nome.lower()}')
print(f'Seu nome possui {len(nome)-nome.count(" ")} letras')
#print(f'Seu primeiro nome possui {nome.find(" ")}') //Diz a posição do primeiro espaço
print(f'Seu primeiro nome é {nome.split()[0].title()} e possui {len(nome.split()[0])} letras')

#strip tira espaços antes e depois
#split separa palavras em listas
#find procura str
#len conta caracteres (espaços contam)
