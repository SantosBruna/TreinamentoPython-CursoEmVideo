#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
maior = menor = 0
posMaior = []
posMenor = []

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

for c, v in enumerate(valores):
    if c == 0:
        maior = menor = v
        posMenor.append(c)
        posMaior.append(c)
    else:
        if maior == v:
            posMaior.append(c)
        if maior < v:
            posMaior = []
            maior = v
            posMaior.append(c)
        if menor == v:
            posMenor.append(c)
        if menor > v:
            posMenor = []
            menor == v
            posMenor.append(c)

print(f'A lista de valores é {valores}')
print(f'O maior elemento é o {maior} e está na posição {posMaior}')
print(f'O menor elemento é o {menor} e ele está na posição {posMenor}')