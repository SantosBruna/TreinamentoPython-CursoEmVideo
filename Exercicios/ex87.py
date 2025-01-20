#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
terceira_coluna = 0
maior = 0

for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = int(input(f'Digite o valor para [{a}, {b}]: '))

print('*'*30)

for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^5}]', end=' ')#o :5 coloca em cinco casas decimais e o ^ deixa o valor centralizado
    print()

for a in range(0, 3):
    for b in range(0, 3):
        if matriz[a][b] % 2 == 0:
            par += matriz[a][b]
        if b == 2:
            terceira_coluna += matriz[a][b]
        if a == 1:
            if maior < matriz[a][b]:
                maior = matriz[a][b]

print('*'*30)
print(f'A soma de todos os valores pares é: {par}')
print(f'A soma de todos os elementos da terceira coluna é {terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior}')
