# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input("Digite um número: "))
fatorial = 1
print('{}! = '.format(num), end='')
while num != 0:
    fatorial *= num
    if num == 1:
        print('{} = {}'.format(num, fatorial), end=' ')
    else:
        print('{}'.format(num), end=' X ')
    num -= 1
