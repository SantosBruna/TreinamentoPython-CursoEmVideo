#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

listaPrincipal = list()
pares = list()
impares = list()
listaPrincipal.append(pares)
listaPrincipal.append(impares)

for num in range(0, 7):
    numero = int(input(f'{num + 1}° Número: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
pares.sort()
impares.sort()
print('*' * 30)
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')
