# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o salário do funcionário R$'))
print('O salário informado é R${}'.format(salario))

if salario > 1250:
    aumento = 10 * salario / 100
    novo_salario = salario + aumento
    print('Com o aumento de R${:.2f}, o salário passa a ser R${:.2f}'.format(aumento, novo_salario))
else:
    aumento = 15 * salario / 100
    novo_salario = salario + aumento
    print('Com o aumento de R${:.2f}, o salário passa a ser R${:.2f}'.format(aumento, novo_salario))