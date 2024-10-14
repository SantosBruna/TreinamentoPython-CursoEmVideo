#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Informe um número: '))

#array = numero.split()


milhar = numero // 1000
restoMilhar = numero % 1000

centena = restoMilhar // 100
restoCentena = numero % 100

dezena = restoCentena // 10
resto = dezena % 100

unidade = numero % 10

print('Analisando o número {} ...'.format(numero))
print('Unidade {}'.format(unidade))
print('Dezena {}'.format(dezena))
print('Centena  {}'.format(centena))
print('Milhar  {}'.format(milhar))
