# Exercício Python 107: Crie um módulo chamado moeda que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from Exercicios.utilidadesCeV import moeda

preco = int(input('Digite um preço: R$ '))
taxa = float(input('Informe a taxa(%): [SOMENTE NUMEROS]'))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumentando {taxa}%, temos R${moeda.aumentar(preco, taxa)}')
