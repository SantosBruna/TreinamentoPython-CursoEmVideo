#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'a lista gerada foi: {numeros}')
print(f'O maior número da lista é {max(numeros)}')
print(f'O menor número da lista é {min(numeros)}')