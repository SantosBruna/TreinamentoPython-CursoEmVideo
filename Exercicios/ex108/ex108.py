#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
# que consiga mostrar os números como um valor monetário formatado.
from Exercicios.utilidadesCeV import moeda

preco = int(input('Digite um preço: R$ '))
taxa = float(input('Informe a taxa(%): [SOMENTE NUMEROS]'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando {taxa}%, temos {moeda.moeda(moeda.aumentar(preco, taxa))}')
