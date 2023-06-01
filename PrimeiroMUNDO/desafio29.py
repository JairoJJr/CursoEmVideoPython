vel = int(input('Qual a velocidade do seu carro?'))
multa =(vel-80)*7
if vel > 80:
    print(f"Você está acima da velocidade permitida da via e recebeu uma multa de {multa} Reais.")
else:
    print('Você está dentro da velocidade da via')


