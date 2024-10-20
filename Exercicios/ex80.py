#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores= []
valor = indiceMenor = indiceMaior = ''
for cont in range(0, 5):
    valor = int(input(f'Digite um valor para a posição {cont}: '))
    if cont == 0 or valor > valores[-1]:
        valores.append(valor)
    else:
        pos = 0
        for pos in range(0, len(valores)):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                break

print(f'Os valores digitados são: {valores}')
