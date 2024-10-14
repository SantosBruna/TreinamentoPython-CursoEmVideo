# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Informe um número inteiro: '))
cont = 0

if numero == 1:
    print('O numero 1 não é um número primo')
elif numero == 2 or numero == 3:
    print('O número {} é um número primo'.format(numero))
elif numero % 2 == 0 and numero > 2:
    print('Números pares maiores que 2 não são números primos, portanto o número {} não é um número primo'.format(numero))
else:
    for c in range(1, numero + 1):
        if numero % c == 0:
            cont += 1
            print('\033[33m', end='')
        else:
            print('\033[31m', end='')
        print('{}'.format(c), end='-> ')
    if cont == 2:
        print('\n\033[mO número {} é divisível por {} números e por isso ele é um número primo'.format(numero, cont))
    else:
        print('\n\033[mO número {} é divisível por {} números e por isso não é um número primo'.format(numero, cont))
