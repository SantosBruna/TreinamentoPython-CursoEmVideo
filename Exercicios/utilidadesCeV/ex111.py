# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from Exercicios.utilidadesCeV import moeda

preco = int(input('Digite um preço: R$ '))
taxa = float(input('Informe a taxa(%) de aumento: [SOMENTE NUMEROS]'))
taxa_reduc = float(input('Informe a taxa(%) de redução: [SOMENTE NUMEROS]'))
moeda.resumo(preco, taxa, taxa_reduc)
