#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros

preco = float(input('Informe o preço das compras: R$'))
print('*'*30)
print('Condições de Pagamento:')
print('[1] à vista dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] em até 2x no cartão')
print('[4] 3x ou mais no cartão')
print('*'*30)
pag = int(input('Informe a condição de pagamento: '))

if pag == 1:
    novoPreco = preco - (10 * preco / 100)
    print('A condição de pagamento informada é à vista dinheiro/cheque.'
          '\nSua compra com 10% desconto ficou em R${:.2f} no total'.format(novoPreco))
elif pag == 2:
    novoPreco = preco - (5 * preco / 100)
    print('A condição de pagamento informada é à vista no cartão.'
          '\nSua compra com 5% desconto ficou em R${:.2f} no total'.format(novoPreco))
elif pag == 3:
    parcela = preco / 2
    print('A condição de pagamento informada é em 2x no cartão.'
          '\nO valor da parcela será de R${:.2f} vai custar R${:.2f} no total.'.format(parcela, preco))
elif pag == 4:
    novoPreco = preco + (20 * preco / 100)
    totalParc = int(input('Qual o total de parcelas? '))
    parcela = novoPreco / totalParc
    print('A condição de pagamento informada é {}x no cartão e terá juros de 20%.'
          '\nO valor da parcela será de R${:.2f} vai custar R${:.2f} no total.'.format(totalParc, parcela, novoPreco))
else:
    print('Opção inválida!')
