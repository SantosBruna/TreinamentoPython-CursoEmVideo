# Exercício Python 110: Adicione o módulo moeda criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from Exercicios.utilidadesCeV import moeda

preco = int(input('Digite um preço: R$ '))
taxa = float(input('Informe a taxa(%) de aumento: [SOMENTE NUMEROS]'))
taxa_reduc = float(input('Informe a taxa(%) de redução: [SOMENTE NUMEROS]'))
moeda.resumo(preco, taxa, taxa_reduc)
