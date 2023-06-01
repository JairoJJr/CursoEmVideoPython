'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.1'''

m = float(input('Digite sua altura em metros '))
cm = m*100
mm = cm*10
print('Sua altura de {:.2f}m é igual a {:.0f}cm e {:.0f}mm'.format(m,cm,mm))


