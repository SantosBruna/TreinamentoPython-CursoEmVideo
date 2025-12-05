# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from Exercicios.utilidadesCeV import moeda

preco = int(input('Digite um preço: R$ '))
taxa = float(input('Informe a taxa(%): [SOMENTE NUMEROS]'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando {taxa}%, temos {moeda.aumentar(preco, taxa, True)}')
print(f'Reduzindo {taxa}%, temos {moeda.diminuir(preco, taxa, True)}')
