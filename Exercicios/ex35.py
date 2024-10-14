#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#a+b>c
#a+c>b
#b+c>a
from time import sleep

print('-=' * 20)
print('Analisador de triângulos!')
print('-=' * 20)
a = float(input('Informe o comprimento da primeira reta: '))
b = float(input('Informe o comprimento da segunda reta: '))
c = float(input('Informe o comprimento da terceira reta: '))
print('-=' * 20)
print('Os comprimentos informados são {}, {} e {}'.format(a, b, c))
print('Analisando os segmentos...')
sleep(1)
print('-=' * 20)

if (a + b) > c and (a + c) >b and (b + c) > a:
    print('As retas podem formar um triângulo!')
else:
    print('As retas informadas NÃO podem formar um triângulo')