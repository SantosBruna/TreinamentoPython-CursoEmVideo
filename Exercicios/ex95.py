#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []
jogadores = []

while True:
    jogador['nome'] = str(input('Informe o nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    jogador.clear()

    resp = str(input('Deseja continuar? [S/N} ')).strip().upper()[0]
    while resp not in 'SsNn':
        print('ERRO! Responda somente S ou N')
        resp = str(input('Deseja continuar? [S/N} ')).strip().upper()[0]
    if resp in 'Nn':
        break

print('-*' * 30)
print('cod   nome                gols          total')
print('-'*60)
for k, v in enumerate(jogadores):
    print(f'{k:<4}', end='')
    for chave, valor in v.items():
        print(f'{str(valor):<15}', end='      ')
    print()
print('-'*60)
while True:
    resp = int(input('Mostrar dados de qual jogador? [999 para parar] '))

    if resp == 999:
        print('<<VOLTE SEMPRE!>>')
        break
    while resp >= len(jogadores):
        print(f'Não existe jogador com o código {resp}')
        resp = int(input('Mostrar dados de qual jogador? [999 para parar] '))
        if resp == 999:
            print('<<VOLTE SEMPRE!>>')
            break

    print(f'--LEVANTAMENTO D0 JOGADOR {jogadores[resp]['nome']}')
    for chave, valor in enumerate(jogadores[resp]['gols']):
        print(f'  => Na partida {chave + 1}, fez {valor} gols.')
    print('-*' * 30)




