#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunoA = input('Informe o nome do primeiro aluno: ')
alunoB = input('Informe o nome do segundo aluno: ')
alunoC = input('Informe o nome do terceiro aluno: ')
alunoD = input('Informe o nome do quarto aluno: ')

lista = [alunoA, alunoB, alunoC, alunoD]
shuffle(lista)
print('A ordem dos alunos é {}'.format(lista))
