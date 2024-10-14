#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

total = prod1000 = precoProdBarato =  0
nomeProdBarato = ''
while True:
    nomeProd = str(input('Nome do produto: '))
    precoProd = float(input('Preço do produto: '))
    total += precoProd
    if precoProd > 1000:
        prod1000 += 1
    if precoProdBarato == 0 or precoProdBarato > precoProd:
        precoProdBarato = precoProd
        nomeProdBarato = nomeProd

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra é R${total:.2f}')
print(f'{prod1000} produtos custam mais de R$1000,00')
print(f'O produto mais barato é {nomeProdBarato} e custa R${precoProdBarato:.2f}')
print('{:-^40}'.format('FIM DO PROGRAMA'))