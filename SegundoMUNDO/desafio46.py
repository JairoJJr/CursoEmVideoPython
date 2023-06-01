#contagem regressiva utilizando biblioteca TIME em Sleep e repetição com for
import time
input('aperte Enter para iniciar a contagem regressiva')

for c in range(10,0,-1):
    print(c)
    time.sleep(1)
print('Feliz Ano NOVO!')