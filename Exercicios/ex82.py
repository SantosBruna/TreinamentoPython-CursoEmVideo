#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
    resp = ' '
    lista.append(int(input('Digite um número inteiro: ')))

    while resp not in 'SsNn':
        resp = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if resp == 'N':
        break

for c in lista:
    if c % 2 == 0:
        pares.append(c)
    elif c % 2 == 1:
        impares.append(c)

print('*' *40)
print(f'A lista gerada é: {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')

