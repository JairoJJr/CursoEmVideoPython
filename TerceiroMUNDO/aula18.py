'''Listas COMPOSTAS'''

teste = []
teste.append('Jairo')
teste.append(28)
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])

print(galera)


pessoas = [['Jairo' , 28],["Jéssica" , 31],["Rafaela" , 14],["Megan" , 3]]
print(pessoas[1][0],pessoas[0])

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')

familia = []
dado = []

for c in range (0, 4):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    familia.append(dado[:])
    dado.clear()
print(familia)

totmai = totmen = 0
for p in familia:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'A família tem {totmai} pessoas maiores e {totmen} pessoas menores.')