#Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média

nota1 = float(input('Digite a primeira nota do aluno'))
nota2 = float(input('Digite a segunda nota do aluno'))

media = (nota1 + nota2)/2

print('A primeira nota é {}, a segunda nota é {} e a média deste aluno é {:.1f}' .format(nota1, nota2, media))


