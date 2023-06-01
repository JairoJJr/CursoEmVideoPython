nome = str(input('Qual é o seu nome? '))
if nome == 'Jairo':
    print('Que nome bonito!')
elif nome.lower() == 'pedro' or nome.lower() == 'maria' or nome.lower() == 'paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome.lower() in 'rafaela jéssica megan':
    print('Você tem o nome de um dos \033[1;31;44mamores\033[m da vida do Jairo. \033[1;31mS2\033[m')
else:
    print('Seu nome é normal.')
print(f'Tenha um bom dia, {nome.title()}')
