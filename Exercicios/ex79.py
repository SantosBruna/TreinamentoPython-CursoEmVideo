#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

valores = list()

while True:
    resp = ' '
    num = int(input('Digite um número inteiro: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! não vou adicionar...')
    while resp not in 'SsNn':
        resp = input('Deseja continuar?[S/N] ').upper().strip()
    if resp == 'N':
        break
valores.sort()
print(f'Os valores digitados são: {valores}')
print('Programa encerrado')
