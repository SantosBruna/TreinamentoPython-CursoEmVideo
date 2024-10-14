# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe o sexo da pessoa: [M/F] ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Opção inválida! digite novamente entre as opções [M/F]: ')).strip().upper()[0]
print('Obrigado!')
