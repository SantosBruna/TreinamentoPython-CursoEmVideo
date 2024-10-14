#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

num = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número de 0 á 5, tente advinhar qual é!')
print('-=-'*20)
sleep(1)
usu = int(input('Em que número eu pensei?  '))
print('VERIFICANDO...')
sleep(2)
if num == usu:
    print('Parabéns! você acertou, conseguiu me vencer!!!')
else:
    print('Eu ganhei! o número era {}, tente uma próxima vez!' .format(num))
