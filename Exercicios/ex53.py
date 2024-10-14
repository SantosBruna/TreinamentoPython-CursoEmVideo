#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Informe uma frase sem utilizar acentos: ').upper().replace(" ", ""))
invertida = frase[::-1]

print('O inverso de {} é {}'.format(frase, invertida))
if frase == invertida:
    print('\033[34mA frase é um palíndromo!')
else:
    print('\033[31mA frase não é um palindromo')
