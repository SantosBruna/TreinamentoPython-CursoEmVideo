#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

print('*'*40)
print('{:^40}'.format(' JOGO DA MEGA SENA '))
print('*'*40)

jogos = int(input('Quantos jogos você quer que eu sortei? '))
total_jogos = []
lista_jogo = []
print()
print('{:>^40}'.format(f'Sorteando {jogos} jogos'))
for jogo in range(0, jogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista_jogo:
            lista_jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    lista_jogo.sort()
    total_jogos.append(lista_jogo[:])
    lista_jogo.clear()
    sleep(1)
    print(f'JOGO {jogo + 1}: {total_jogos[jogo]}')
print('{:>^40}'.format('BOA SORTE!!'))
