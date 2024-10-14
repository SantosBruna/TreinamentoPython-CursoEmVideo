#Crie um algoritmo que leia um número e mostre o
# seu dobro, o seu triplo e a raiz quadrada

num = float(input('Digite um número: '))

dobro  = num * 2
triplo = num * 3
raiz   = num ** (1/2)

print('O número digitado é {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}' .format(num, dobro, triplo, raiz))
