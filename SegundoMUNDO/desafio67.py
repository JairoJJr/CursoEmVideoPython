'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número for negativo.'''



while True:
    n = int(input('''Digite um número positivo para ver a tabuada correspondente:
      [Digite um número menor que zero para sair]'''))
    if n < 0:
        break
    for i in range (0 , 11 , 1):
        print(f'{n} X {i} = {n*i}')
    print(10*'-=-=')
    
print('FIM')
