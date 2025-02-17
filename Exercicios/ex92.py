#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime
pessoa = {}
pessoa['Nome'] = str(input('Informe o nome: '))
ano = int(input('Informe o ano de nascimento: '))
hoje = datetime.date.today().year
pessoa['idade'] = hoje - ano
pessoa['ctps'] = int(input('Informe o número da carteira de trabalho (0 se não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Informe o ano de contratação: '))
    pessoa['salario'] = float(input('Informe o salário: R$'))
    pessoa['aposentadoria'] = ((pessoa['contratacao'] + 35) - hoje) + pessoa['idade']
print('-*' * 30)
for k, v in pessoa.items():
    print(f'  * {k} tem o valor de {v}')


