'''Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.'''

maistermos = 1
ct = 10

pt = int(input('Digite o primeiro termo: '))
rpa = int(input('Digite a razão da PA: '))
dec = pt  + (10-1) * rpa
for c in range (pt , dec + rpa , rpa):
    print(c , end = '->')
print('\n')
print(c)

while maistermos != 0:
    maistermos = (int(input('Deseja ver mais quantos termos? ')))
    ct += maistermos
    fimrange = (c + (maistermos - 1) * rpa) + rpa
    for i in range (c , fimrange, rpa):
        print(i , end = '->')
    print('\n')

print(f'Progressão finalizada com {ct} termos mostrados.')