#Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(lar, com):
    area = lar * com
    print(f'A área de um terreno {lar}X{com} é de {area}m²')


def titulo(txt):
    print(txt)
    print('-' * len(txt))

# programa principal


titulo('Controle de Terrenos')
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))
area(lar, com)
