'''Tuplas'''
#tuplas são imutáveis
lanche = ('Hambúrguer' , 'Suco' , 'Pizza' , "Pudim")
print(lanche[0:3])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print("comi muito")

for cont in range(0 , len(lanche)):
    print(f'Comerei {lanche[cont]}')
print("comi de novo.")

a = (2 , 5 , 4)
b = (5 , 8 , 1 , 2)
c = b + a
print(c)
print(c.index(8))
print(c.count(5))