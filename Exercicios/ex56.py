# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

total_idade = 0
homem_idade = 0
homem_nome = ''
total_mulheres = 0

for c in range(1, 5):
    print('------- {}° PESSOA -------'.format(c))
    nome = str(input('Informe o nome da pessoa: ')).strip()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o gênero da pessoa[M/F]: ')).strip()

    if idade > homem_idade and sexo in 'Mm':
        homem_idade = idade
        homem_nome = nome
    elif idade < 20 and sexo in 'Ff':
        total_mulheres += 1
    total_idade += idade

print('A média de idade do grupo é {}'.format(total_idade / 4))
print('O nome do homem mais velho é {} e a sua idade é {}'.format(homem_nome, homem_idade))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(total_mulheres))
