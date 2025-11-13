#Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    print('*-' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)

    if passo == 0:
        passo = 1

    if passo > 0 and fim < inicio:
        passo = -passo
    elif passo < 0 and inicio < fim:
        passo = -passo

    for cont in range(inicio, fim, passo):
        print(cont, end=' ')
        sleep(0.5)
    print(fim, end=' ')
    sleep(0.5)
    print(' => FIM!')


def lerParams():
    print()
    print('-' * 30)
    print('Personalize a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('-' * 30)
    contador(inicio, fim, passo)




# principal
contador(1, 10, 1)
contador(10, 0, 2)
lerParams()
