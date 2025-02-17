#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = {}
dados = []
total_idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper()

    while pessoa['sexo'] not in 'MmFf':
        print('ERRO!!! Por favor digite apenas M ou F')
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper()

    pessoa['idade'] = int(input('Idade: '))
    dados.append(pessoa.copy())

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp not in 'SsNn':
        print('ERRO!!! Responda apenas S ou N, por favor!')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp in 'Nn':
        break
for pessoa in dados:
    for k, v in pessoa.items():
        if k == 'idade':
            total_idade += v
media = total_idade/len(dados)
acima_media = []
print('-*' * 30)
print(f'Ao todo temos {len(dados)} pessoas cadastradas')
print(f'A média de idade é {media:.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for pessoa in dados:
    for k, v in pessoa.items():
        if k == 'sexo' and v == 'F':
            print(f'{pessoa["nome"]}', end=' ')
        if k == 'idade' and v > media:
            acima_media.append(pessoa.copy())

print()
print(f'Lista das pessoas que estão acima da média: ')
for pessoa in acima_media:
    for chave, valor in pessoa.items():
        print(f'{chave} = {valor}; ', end=' ')
    print()
