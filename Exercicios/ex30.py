#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Informe um número '))

resultado = num % 2

if resultado == 0 :
    print('O número informado é {} e ele é par'.format(num))
else:
    print('O número informado é {} e ele é ímpar'.format(num))
