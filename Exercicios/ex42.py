#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes
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
    if a == b == c:
        print('O triângulo é equilátero!')
    elif a != b!= c != a :
        print('O triângulo é escaleno!')
    else:
        print('O triangulo é iósceles!')
else:
    print('As retas informadas NÃO podem formar um triângulo')


