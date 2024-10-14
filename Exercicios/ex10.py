# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# 1 dolar equivale a R$5,24

valor = float(input("Quanto de dinheiro você tem? R$"))
Dolar = 5.24

print("Com R${:.2f} você possui US${:.2f}".format(valor, valor/Dolar))
