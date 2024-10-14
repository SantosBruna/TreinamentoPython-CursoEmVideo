#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

alunoA = input('Informe o nome do primeiro aluno: ')
alunoB = input('Informe o nome do segundo aluno: ')
alunoC = input('Informe o nome do terceiro aluno: ')
alunoD = input('Informe o nome do quarto aluno: ')

lista = [alunoD, alunoA, alunoC, alunoB]
escolhido = choice(lista)
print('O aluno escolhido é {} '.format(escolhido))
