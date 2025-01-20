#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0], [0,0,0], [0,0,0]]

'''for cont in range(0, 9):
    matriz[cont] = int(input(f'Digite o valor: '))
'''
for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = int(input(f'Digite o valor para [{a}, {b}]: '))

for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^5}]', end=' ')#o :5 coloca em cinco casas decimais e o ^ deixa o valor centralizado
    print()


#isabelpage
