# Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras aotodo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

nome = str(input('Informe o seu nome completo ')).strip()

array = nome.split()
totalArray = len(array)
total = len(nome) - (nome.count(' '))

print('Analisando o seu nome...')
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('A quantidade de letras que o nome tem ao todo é: {}'.format(total))
print('A quantidade de letras que tem no primeiro nome é: {}' . format(len(array[0])))
