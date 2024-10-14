#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


print('-=-' * 20)
print('Aprovação de empréstimo bancário!')
print('-=-' * 20)
casa = float(input('Informe o valor da casa que deseja comprar: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = int(input('Em quantos anos deseja pagar a casa? '))

prestacaoDoSalario = 30 * salario / 100
prestacaoMensal = casa / (anos * 12)

if prestacaoDoSalario < prestacaoMensal:
    print('A parcela do seu empréstimo ficou em R${:.2f} o que ultrapassa os 30% do seu salario'.format(prestacaoMensal))
    print('Infelizmente seu emprestimo será negado.')
else:
    print('A parcela do seu empréstimo ficou em R${:.2f}. Parabéns! empréstimo aprovado!'.format(prestacaoMensal))
