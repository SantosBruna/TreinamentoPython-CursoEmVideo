#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []
alunos = []
while True:
    nome = str(input('Nome: ')).strip()
    nota_1 = float(input('Primeira nota: '))
    nota_2 = float(input('Segunda nota: '))
    media = (nota_1 + nota_2) / 2
    lista.append(nome)
    lista.append([nota_1, nota_2])
    lista.append(media)
    alunos.append(lista[:])
    lista.clear()
    resp = input('Deseja continuar? [S/N]').strip().upper()
    if resp in 'Nn':
        break
print('*'*40)
print('N°', '{:^15}'.format('NOME'), 'MEDIA')
print('-'*40)
for i, l in enumerate(alunos):
    print(f'{i}', '{:^15}'.format(f'{l[0]}'), f'{l[2]}')
print('-'*40)

while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 Interrompe)'))
    if aluno == 999:
        break
    print(f'As notas do {alunos[aluno][0]} são {alunos[aluno][1]}')

