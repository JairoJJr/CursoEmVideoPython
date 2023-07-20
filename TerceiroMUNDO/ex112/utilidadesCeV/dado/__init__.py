def leiaDinheiro(msg):
    válido = False
    while not válido:
        num = str(input(msg)).replace(',','.').strip()
        if num.isalpha() or num == '':
            print(f'\033[0;31mERRO: "{num}" é um preço inválido!\033[m')
        else:
            válido = True
            preço = float(num)
            return preço
    
    

