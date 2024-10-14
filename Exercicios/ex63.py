#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

num = int(input('Digite um número: '))
fib = 1
fib_antecessor = 0
cont = 3
print('{} - {}'.format(fib_antecessor, fib), end=' - ')

while cont <= num:

    atual = fib_antecessor + fib
    fib_antecessor = fib
    fib = atual
    cont += 1
    print('{}'.format(fib), end=' - ')
print('FIM', end='')
