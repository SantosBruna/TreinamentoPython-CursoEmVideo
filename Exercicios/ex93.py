#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []
jogador['Nome'] = str(input('Informe o nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-*' * 30)
print(jogador)
print('-*' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-*' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')
for k, v in enumerate(jogador['gols']):
    print(f'  => Na partida {k + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

