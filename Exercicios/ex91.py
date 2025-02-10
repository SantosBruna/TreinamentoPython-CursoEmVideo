#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from operator import itemgetter
from random import randint
from time import sleep
jogadores = {}


for v in range(1, 5):
    jogadores['jogador' + str(v)] = randint(1, 6)

print('Valores Sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

jogadores_ordenados = {chave: jogadores[chave] for chave in sorted(jogadores, key=itemgetter(1), reverse=True)}
cont = 1
print('-='*30)
print('==RANKING DOS JOGADORES==')
cont = 1

for k, v in jogadores_ordenados.items():
    print(f'{cont}° lugar: {k} com {v}')
    sleep(1)
    cont += 1

#outra solução seria:
#ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True
#for i, v in enumerate(ranking):
#   print(f'{i + 1} lugar: {v[0]} com {v[1]}.'}
#   sleep(1)








