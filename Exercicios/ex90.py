#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['Nome'] = str(input("Informe o nome do aluno: ")).strip()
aluno['media'] = float(input(f"Informe a média do {aluno['Nome']}: "))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] > 3:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('*'*40)
for k, v in aluno.items():
    print(f'- O {k} é igual a {v}')
