#Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milimetros

valor = float(input('Informe um valor em metros: '))

centimetros = valor * 100
milimetros  = valor * 1000

print('O valor em metros é: {}, em centímetros é {} e em milímetros é {}' .format(valor, centimetros, milimetros))
