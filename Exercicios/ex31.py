#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input('Informe a distância em KM da viagem: '))

if viagem <= 200:
    preco = 0.50 * viagem
else:
    preco = 0.45 * viagem

#preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45

print('A sua viagem de {:.0f}Km custará R${:.2f}'.format(viagem, preco))
