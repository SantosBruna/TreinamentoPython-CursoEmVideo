#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot

catA = float(input('Informe o comprimento do cateto oporto: '))
catB = float(input('Informe o comprimento do cateto adjacente: '))

hipo = hypot(catA, catB)#também pode ser obtido com a seguinte formula: (catA ** 2 + catB ** 2) **1/2
print('O comprimento da Hipotenusa é {:.2f}'.format(hipo))
