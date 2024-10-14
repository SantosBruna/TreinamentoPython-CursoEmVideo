# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Informe o salário do funcionário: R$'))

aumento = salario * 15 / 100

print('O salario do funcionário é de R${:.2f} com 15% de aumento é R${:.2f}'.format(salario, salario + aumento))
