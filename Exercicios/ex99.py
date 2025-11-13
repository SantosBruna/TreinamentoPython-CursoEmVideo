#Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep
def maior(*lst):
    maior = 0
    for num in lst:
        if int(num) > maior:
            maior = num
    print(f'O maior valor informado foi {maior}')

def exibeLista(*lst):
    for num in lst:
        print(num, end=' ')
        sleep(0.5)

def interacao(*valores):
    print('*-' * 30)
    print('Analisando os valores passados ...')
    sleep(1)
    exibeLista(*valores)
    print(f'foram informados, {len(valores)} valores ao todo')
    maior(*valores)


# principal
interacao(2, 9, 4, 5, 7, 1)
interacao(4, 7, 0)
interacao(1, 2)
interacao(6)
interacao()
