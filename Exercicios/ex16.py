#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

num = float(input('Informe um número: '))

inteiro = trunc(num)#também pode ser usado o int()

print('A parte inteira do número {} é {}'.format(num, inteiro))
