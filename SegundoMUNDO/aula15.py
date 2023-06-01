'''Interrompendo laços de repetição.'''
'''Comando break'''

n = s = 0

while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
print(s)    
print('FIM')
