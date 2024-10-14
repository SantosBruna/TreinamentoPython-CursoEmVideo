#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais

a = int(input('Informe um número inteiro: '))
b = int(input('Informe outro número inteiro: '))

if a > b:
    print('O número {} é maior que {}'.format(a, b))
elif b > a:
    print('O número {} é maior que {}'.format(b, a))
else:
    print('Os números são iguais!')
