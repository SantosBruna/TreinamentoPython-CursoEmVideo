# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

num = randint(0, 10)
cont = 1
print('-=-'*20)
print('Vou pensar em um número de 0 á 10, tente advinhar qual é!')
print('-=-'*20)
sleep(1)
usu = int(input('Em que número eu pensei?  '))

while num != usu:
    print('VERIFICANDO...')
    sleep(1)
    if num < usu:
        print('Menos... Tente mais uma vez!')
        usu = int(input('Em que número eu pensei?  '))
    else:
        print('Mais... Tente mais uma vez!')
        usu = int(input('Em que número eu pensei?  '))
    cont += 1
print('Parabéns! você acertou, conseguiu me vencer!!!')
print('Você precisou de {} palpites para conseguir me vencer!'.format(cont))

