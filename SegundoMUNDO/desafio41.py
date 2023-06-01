'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

import datetime

nsc = int(input("Digite seu ano de nascimento: "))
idade = datetime.datetime.today().year - nsc

if idade <= 9:
    print(f"O atleta tem {idade} anos.\nClassificação: MIRIM")
if 9 < idade <= 14:
    print(f"O atleta tem {idade} anos.\nClassificação: Infantil")
if 14 < idade <=19:
    print(f"O atleta tem {idade} anos.\nClassificação: Júnior")
if 19 < idade <= 25:
    print(f"O atleta tem {idade} anos.\nClassificação: Sênior")
if 25 < idade:
    print(f"O atleta tem {idade} anos.\nClassificação: Master")

