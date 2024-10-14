#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Informe a largura da parede em metros: "))
altura = float(input("Informe a altura da parede em metros: "))

area = largura * altura
tinta = area/2

print("A sua parede tem a dimensão de {}X{} e a sua área é {:.3f} m²\nVocê irá precisar de {:.3f}l de tinta".format(largura, altura, area, tinta))
