#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Informe o peso da {}° pessoa: '.format(c)))

    if c == 1:
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso informado é {}kg'.format(maior))
print('O menor peso informado é {}kg'.format(menor))
