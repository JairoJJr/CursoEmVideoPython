'''DICIONÁRIOS'''
#Índices literais / São identificados por {}
#append não funciona, é só referenciar e atribuir.
#Na hora de declarar usa chaves, mas na hora de referenciar usa colchetes.

dados = {}
#ou dados = dict()

dados = {'nome' : 'Pedro', 'idade' : 25}
dados['sexo'] = "M"
print(dados['nome'])

filme = {'titulo': 'Jurassic Park',
         'ano': 1993,
         'diretor': 'Spielberg'
}
print(filme.keys())
print(filme.values())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}.')

#Prática

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(estado1)
#print(estado2)
#print(brasil)
#print(brasil[0])
#print(brasil[1])
#print(brasil[0]['uf'])

estado = {}
brasil = []

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v,end=' ')
    print()