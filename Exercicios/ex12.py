#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Informe o preço do produto: R$'))

desconto = (preco * 5)/100

print('O preço informado é R${:.2f}, 5% de desconto equivale a R${:.2f}. O novo preço do produto é R${:.2f}'.format(preco, desconto, preco - desconto))


