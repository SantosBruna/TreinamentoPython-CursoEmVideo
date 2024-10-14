# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
from datetime import date

ano_atual = date.today().year
cont = 0
for c in range(1, 8):
    ano = int(input('Informe o ano de nascimento da pessoa {}: '.format(c)))
    idade = ano_atual - ano
    if idade >= 21:
        cont += 1
print('Das 7 pessoas informadas {} são maiores de idade e {} não atingiram os 21 anos.'.format(cont, 7 - cont))
