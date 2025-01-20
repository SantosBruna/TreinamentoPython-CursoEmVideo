#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
lista = list()
nomeLeves = list()
nomePesados = list()
pesado = leve = 0

while True:
    resp = ' '
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))

    if pesado == leve == 0:
        pesado = peso
        leve = peso
    else:
        if pesado < peso or pesado == peso:
            pesado = peso
            nomePesados.append(nome)
        elif leve > peso or leve == peso:
            leve = peso
            nomeLeves.append(nome)

    pessoas.append(nome)
    pessoas.append(peso)
    lista.append(pessoas[:])
    pessoas.clear()

    while resp not in 'SsNn':
        resp = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if resp == 'N':
        break

print(f'A lista com as {len(lista)} pessoas cadastradas foram: {lista}')
print(f'\nO maior peso foi {pesado}Kg de {nomePesados}\nO mais leve foi {leve}Kg de {nomeLeves}')
