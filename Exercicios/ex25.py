# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Informe o seu nome completo: ')).strip()
result = 'SILVA' in nome.upper()
print(result)