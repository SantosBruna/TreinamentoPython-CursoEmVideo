#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Informe o seu nome completo: ')).strip()

lista = nome.split()
total = len(lista)
print('O primeiro nome informado é {}'.format(lista[0]))
print('O último nome informado é {}'.format(lista[total - 1]))
