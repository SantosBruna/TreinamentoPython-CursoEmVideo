#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.


from random import randint
numeros = list()

def sorteia():
    print(f'Sorteando 5 valores para a lista: ', end='')
    for i in range(0, 5):
        num = randint(1, 9)
        print(f' {num}', end='')
        numeros.append(num)
    print()
    print(f'A lista sorteada é: {numeros}')

def somaPar():
    soma = 0
    sorteia()
    for num in numeros:
        if ((num % 2) == 0):
            soma = soma + num
    print(f'A soma entre os numeros pares sorteados são: {soma}')


somaPar()