# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'
maior = soma = cont = 0
while continuar == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    continuar = str(input('Deseja continuar digitando números? [S/N]')).strip().upper()[0]
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))
print('Você digitou {} e a média entre eles é {}'.format(cont, soma / cont))
