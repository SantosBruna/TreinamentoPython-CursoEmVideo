#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km o carro percorreu? '))
dias = float(input('O carro foi alugado por quantos dias? '))

valorDia = 60 * dias
valorKm = km * 0.15

debito = valorDia + valorKm

print('O valor a pagar é R${:.2f}'.format(debito))
