#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan

angulo = float(input('Informe o angulo: '))
radi = radians(angulo)

seno = sin(radi)
cos = cos(radi)
tang = tan(radi)

print('O angulo informado foi {}\nO seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2}'.format(angulo, seno, cos, tang))
