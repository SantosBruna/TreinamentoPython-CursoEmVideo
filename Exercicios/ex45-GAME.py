#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

print('{:*^40}'.format(' JOKENPÔ '))
print('''Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
lista = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Qual opção você escolhe? '))
pc = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=-'*20)
print('Computador escolheu {}'.format(lista[pc].upper()))
print('Jogador escolheu {}'.format(lista[jogador].upper()))
print('-=-'*20)

if (jogador == 0  and pc == 2) or (jogador == 1 and pc == 0) or (jogador == 2 and pc == 1):
    print('JOGADOR VENCE!')
elif (jogador == 0 and pc == 1) or (jogador == 1 and pc == 2) or (jogador == 2 and pc == 0):
    print('COMPUTADOR VENCE!')
elif (jogador) == pc:
    print('EMPATADOS!')
elif jogador > 3:
    print('Opção errada, escolha novamente')


