dist = int(input("Qual a distância da sua viagem? "))
if dist <= 200:
    print(f"Sua passagem de ônibus custará R${(dist/2):.2f}.")
else:
    print(f"Sua passagem de ônibus custará R${(dist*0.45):.2f}.")