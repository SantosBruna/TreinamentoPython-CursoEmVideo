#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser
# sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

notas = (50, 20, 10, 1)
celulas = []
while True:
    falta = valor = int(input('Qual será o valor a ser sacado? R$'))
    for c in range(0, 4):
        if falta >= notas[c]:
            celulas.append(falta // notas[c])
            falta = max(falta - (celulas[c] * notas[c]), 0)
            print(f'Você receberá {celulas[c]} notas de {notas[c]} reais')
        else:
            celulas.append(0)
    if falta == 0:
       break

