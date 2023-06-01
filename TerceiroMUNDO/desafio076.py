'''Crie um programa que tenha uma tupla única com os nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos = ('Lápis',1.75,
            'Borracha',2,
            'Caderno',15.9,
            'Estojo',25)

for pos in range(0 , len(produtos)):
    if pos % 2 == 0 :
        print(f'{produtos[pos]:.<25}', end = " ")
    else:
        print(f'R${produtos[pos]:>6.2f}')

