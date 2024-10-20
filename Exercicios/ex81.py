#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    resp = ' '
    num = int(input('Digite um número inteiro: '))
    lista.append(num)

    while resp not in 'SsNn':
        resp = input('Deseja continuar?[S/N] ').upper().strip()
    if resp == 'N':
        break

lista.sort(reverse=True)
print('*'*40)
print(f'A quantidade de números digitados é {len(lista)}')
print(f'A lista criada em ordem decrescente é: {lista}')

if 5 in lista:
    print(f'O número 5 está lista!')
else:
    print(f'O número 5 não faz parte da lista.')

